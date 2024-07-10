import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200


def test_send_message(client):
    rv = client.post('/send', data=dict(
        username='testuser',
        message='Hello, world!'
    ), follow_redirects=True)
    assert rv.status_code == 200
    assert b'testuser' in rv.data
    assert b'Hello, world!' in rv.data
