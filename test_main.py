from fastapi.testclient import TestClient

# import our app from main.py

from main import app

# Instantiate the testing client with our app
client = TestClient(app)

# Write tests same as in reqests module
def test_api_locally_get_root():
    r = client.get("/")
    assert r.status_code == 200