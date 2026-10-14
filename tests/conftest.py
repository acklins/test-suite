import pytest

from fastapi.testclient import TestClient

from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

from sqlalchemy.orm import sessionmaker, Session

from app.database import Base, get_db
from app.models.task import Task
from app.main import app

#In-memory SQLite test db
TEST_DATABASE_URL = "sqlite:///:memory:"

test_engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
#Step 2: Create the test session factory
TestingSessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=test_engine,
)               
#pytest finds client fixture & returns a FastAPI TestClient.
@pytest.fixture
def client():
    #Create tables before each test
    Base.metadata.create_all(bind=test_engine)

    def override_get_db():
        db: Session = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()
    #Replace the dev db dependency.
    app.dependency_overrides[get_db] = override_get_db

    try:
        #Provide the TestClient to pytest.
        with TestClient(app) as test_client:
            yield test_client #this passes the TestClient instance to the tests
    finally:
        # Clean up after each test
        app.dependency_overrides.pop(get_db, None)
        Base.metadata.drop_all(bind=test_engine)