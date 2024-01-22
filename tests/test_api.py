from fastapi.testclient import TestClient
import os
import sys

# Add parent directory to path to allow importing app
parent_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(parent_dir, '..'))

# Import app
from webserver import app

client = TestClient(app)

def test_search_movies_success():
    response = client.get("/search-movies/?title=Inception")
    assert response.status_code == 200
    assert len(response.json()) > 0  # Assuming Inception is in the database

def test_search_movies_no_title():
    response = client.get("/search-movies/")
    assert response.status_code == 422

def test_search_movies_not_found():
    response = client.get("/search-movies/?title=NonExistingMovie")
    assert response.status_code == 404
