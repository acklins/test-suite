# Task CRUD API test suite
#Run: python3 -m pytest tests/ -v

def test_create_task(client):
    #Arrange
    task_data = {
        "title": "Buy groceries", 
        "completed": False,
    }
    #Act
    response = client.post("/tasks/", json=task_data)

    #Assert
    assert response.status_code == 201
    assert response.json()["title"] == "Buy groceries"
    assert response.json()["completed"] is False
    assert "id" in response.json()

def test_list_tasks(client):
    #Arrange
    client.post(
        "/tasks/", 
        json={"title": "Read a book"},
    )
    #Act
    response = client.get("/tasks/")

    #Assert
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == "Read a book"

def test_get_task_by_id(client):
    #Arrange
    create_response = client.post(
        "/tasks/", 
        json={"title": "Finish api homework"},
    )
    assert create_response.status_code == 201
    task_id = create_response.json()["id"]

    #Act
    response = client.get(f"/tasks/{task_id}")

    #Assert
    assert response.status_code == 200
    assert response.json()["id"] == task_id
    assert response.json()["title"] == "Finish api homework"

#Testing api error handling
def test_get_nonexistent_task_returns_404(client):
#Act
    response = client.get("/tasks/9999")  
   
#Assert 
    assert response.status_code == 404
    assert response.json()["detail"] == "Task 9999 not found"

def test_patch_task(client):
    #Arrange
    create_response = client.post(
        "/tasks/", 
        json={
            "title": "Clean laptop",
            "description": "Organize notes",
            "completed": False,
        },
    )
    assert create_response.status_code == 201
    task_id = create_response.json()["id"]

    #Act
    response = client.patch(
        f"/tasks/{task_id}", 
        json={"completed": True},
    )

    #Assert
    assert response.status_code == 200
    assert response.json()["completed"] is True
    assert response.json()["title"] == "Clean laptop"
    assert response.json()["description"] == "Organize notes"

def test_delete_task(client):
    #Arrange
    create_response = client.post(
        "/tasks/", 
        json={"title": "Go grocery shopping"},
    )
    assert create_response.status_code == 201
    task_id = create_response.json()["id"]

    #Act
    delete_response = client.delete(f"/tasks/{task_id}")

    #Assert
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == f"Task {task_id} deleted"

    #Verify the task is gone
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404

def test_create_task_invalid_data_returns_422(client):
#Arrange
    invalid_task = {"title":""}
        
    #Act
    response = client.post("/tasks", json=invalid_task)

    #Assert
    assert response.status_code == 422
    assert "detail" in response.json()

def test_duplicate_task_title_returns_409(client):
#Arrange
    task_data = {"title": "Unique Task"}

    first_response = client.post(
        "/tasks/", 
        json=task_data,
    )
    assert first_response.status_code == 201
#Act
    second_response = client.post(
        "/tasks/", 
        json=task_data,
    )
#Assert
    assert second_response.status_code == 409
    assert second_response.json()["detail"] == (
        "A task with that title already exists"
    )
                                                   
