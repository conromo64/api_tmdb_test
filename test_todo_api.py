#pytest -s -m test_auth
import pytest
import requests

ENDPOINT = "https://todo.pixegami.io"

@pytest.mark.test_can_call_api
def test_can_call_api():
    print('---------------------------------test_todo---------------------------------------------')
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

@pytest.mark.test_can_create_task
def test_can_create_task():
    payload= new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    
    data = create_task_response.json()
    print("----data",data)

    task_id = data["task"]["task_id"]
    print('----task_id ',task_id)
    get_task_response = get_task(task_id)

    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    print("----get_task_data",get_task_data)
    print(get_task_data["content"])

    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]

@pytest.mark.test_can_update_task
def test_can_update_task():
    payload= new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]
    new_payload = {
        "user_id": payload["user_id"],
        "task_id": task_id,
        "content": "my update content",
        "is_done": True, 
    }
    update_task_response = update_task(new_payload)
    print("update_task_response.status_code ",update_task_response.status_code)
    assert update_task_response.status_code == 200 

    get_task_resp = get_task(task_id)
    get_task_data = get_task_resp.json()
    print("----get_task_data",get_task_data)
    print("----data.content ",get_task_data["content"])

    #assert get_task_data["content"] == payload["content"]
    #assert get_task_data["user_id"] == payload["user_id"]


def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)

def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)

def get_task(task_id):
    print('----liga ',ENDPOINT + f"/get-task/{task_id}")
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

def new_task_payload():
    return {
        "content": "my test content",
        "user_id": "test_user",
        "task_id": "test_task_id",
        "is_done": False,
    }
