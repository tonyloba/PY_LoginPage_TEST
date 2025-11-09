from utils.api_client import APIClient

def test_get_post():
    client = APIClient("https://jsonplaceholder.typicode.com")
    response = client.get("posts/1")

    assert response.status_code == 200
    data = response.json()

    assert data["id"] == 1
    assert "title" in data
