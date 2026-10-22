"""
Tests for Flask application and routing.
"""

import pytest
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).parent.parent.absolute()
sys.path.insert(0, str(PROJECT_ROOT))

import app

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_index_route(client):
    """Test home route responds correctly."""
    response = client.get('/')
    assert response.status_code == 200

def test_roadmap_route(client):
    """Test roadmap route responds correctly."""
    response = client.get('/roadmap')
    assert response.status_code == 200

def test_pdf_route(client):
    """Test PDF library route responds correctly."""
    response = client.get('/pdf')
    assert response.status_code == 200

def test_tutor_route(client):
    """Test tutor route responds correctly."""
    response = client.get('/tutor')
    assert response.status_code == 200

def test_datasets_route(client):
    """Test datasets route responds correctly."""
    response = client.get('/datasets')
    assert response.status_code == 200

def test_training_route(client):
    """Test training route responds correctly."""
    response = client.get('/training')
    assert response.status_code == 200

def test_progress_route(client):
    """Test progress route responds correctly."""
    response = client.get('/progress')
    assert response.status_code == 200

def test_settings_route(client):
    """Test settings route responds correctly."""
    response = client.get('/settings')
    assert response.status_code == 200
