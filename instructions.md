# Test Suite

**Module:** 5 — FastAPI Development
**Estimated time:** 45 minutes

## Objective

Write a comprehensive test suite for a pre-built Task CRUD API using pytest and FastAPI's TestClient, with an isolated in-memory test database.

## What You'll Do

1. In `tests/conftest.py`, set up the test infrastructure:
   - Create an in-memory SQLite test engine using `StaticPool`.
   - Create a `TestingSessionLocal` session factory.
   - Define a `client` pytest fixture that creates tables, overrides `get_db` with the test session using `app.dependency_overrides`, yields a `TestClient`, and cleans up afterward.
2. In `tests/test_tasks.py`, implement 8 tests following the AAA (Arrange/Act/Assert) pattern:
   - `test_create_task` — POST creates a task and returns 201.
   - `test_list_tasks` — GET returns 200 and a list.
   - `test_get_task_by_id` — GET by ID returns the correct task.
   - `test_get_nonexistent_task_returns_404` — GET with invalid ID returns 404.
   - `test_patch_task` — PATCH updates only specified fields.
   - `test_delete_task` — DELETE removes the task (verify with follow-up GET).
   - `test_create_task_invalid_data_returns_422` — POST with empty title returns 422.
   - `test_duplicate_task_title_returns_409` — POST with duplicate title returns 409.

## Starter Code

```
app/                     — Complete Task CRUD API (do not modify)
  __init__.py
  main.py
  database.py
  models/
    __init__.py
    task.py
  schemas/
    __init__.py
    task.py
  routers/
    __init__.py
    tasks.py
tests/
  __init__.py
  conftest.py            — Test fixture stubs to complete
  test_tasks.py          — Eight test function stubs to implement
```

The `app/` code is fully working. Your task is to write the tests, not modify the application.

## Running

```bash
pytest tests/ -v
```

## Deliverable

A passing test suite with 8+ tests covering happy paths, error cases (404, 409, 422), and the dependency override pattern for database isolation.
