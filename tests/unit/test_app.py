"""
This file (test_app.py) contains the unit tests for the app.py file.
"""
from flaskr import app


def test_index_page():
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'Flask Stock Portfolio App' in response.data
        assert b'Welcome to the Flask Stock Portfolio App!' in response.data