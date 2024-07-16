import pytest
from app import create_app, db
from app.models import QnA
import os
@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        'TESTING': True,
    })

    with app.app_context():
        yield app


@pytest.fixture
def client(app):
    return app.test_client()

def test_ask_question(client, mocker):
    mocker.patch('app.openai_client.get_answer', return_value="mocked answer")
    response = client.post('/ask', json={'question': 'What is docker?'})
    data = response.get_json()
    assert response.status_code == 200
    assert 'question' in data
    assert 'answer' in data

