import requests
from jsonschema import validate
from utils.schemas import user_schema


def test_user_schema_validation():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = response.json()

    # Validate structure matches schema
    validate(instance=data, schema=user_schema)

    assert response.status_code == 200
