# Task CRUD API — Automated Testing

## Project Overview

This project demonstrates automated testing of a FastAPI Task CRUD API using pytest, FastAPI TestClient, SQLAlchemy, and an isolated in-memory SQLite database.

The application code was provided as part of Module 5. The assignment focuses on implementing automated tests without modifying the existing API.

## Test Coverage

**Coverage target:** 80%

**Actual coverage:** 93% 

**Test results:** 11 passed 

### Coverage Report

Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
app/__init__.py                0      0   100%
app/database.py               13      4    69%   19-23
app/main.py                    9      2   78%    15-16
app/models/task.py            10      0   100%
app/routers/tasks.py          44      0   100%   
app/schemas/task.py           12      0   100%
--------------------------------------------------------
TOTAL                         88      6    93%

## Tests Implemented

The automated test suite covers:

- Creating a task successfully (201)
- Listing tasks (200)
- Retrieving a task by ID (200)
- Retrieving a nonexistent task (404)
- Partially updating a task (200)
- Deleting a task and verifying removal (200/404)
- Rejecting invalid task data (422)
- Rejecting duplicate task titles (409)
- Rejecting updates to nonexistent tasks (404)
- Rejecting deletion of nonexistent tasks (404)
- Rejecting titles longer than 200 characters (422)

## Test Database Isolation

Tests use an in-memory SQLite database configured with SQLAlchemy's StaticPool.

The pytest client fixture overrides FastAPI's get_db dependency, ensuring tests do not modify the development database.

Database tables are created before each test and removed afterward.

## Running Tests

Install dependencies:

python3 -m pip install fastapi sqlalchemy pytest pytest-cov httpx

Run the tests:

python3 -m pytest tests/ -v

Run tests with coverage reporting:

python3 -m pytest tests/ -v --cov=app --cov-report=term-missing

## Conclusion

The test suite verifies the Task CRUD API's main functionality, input validation, error handling, and database isolation. The coverage report identifies which application statements were executed and where additional tests may be useful.
