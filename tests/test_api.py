import requests


def test_get_todo():
    url = "https://jsonplaceholder.typicode.com/todos/1"

    response = requests.get(url)

    assert response.status_code == 200
    assert response.json()["id"] == 1