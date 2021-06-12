"""
This file (test_routes.py) contains the unit tests for the routes.py file.
"""
from werkzeug.wrappers import response
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
        assert b'<h1>Quick Search' in response.data
        assert b'<li>set up some lookup' in response.data
        assert b'<form method="post" action=""' in response.data
        assert b'<input name="address1" type="text" required' in response.data
        assert b'<input name="key" type="text" placeholder="key location" required' in response.data
        assert b'<button type="submit' in response.data

def test_post_index_page():
    """
    GIVEN a flask app
    WHEN the '/ page is posted to 'POST`
    THEN check that the data is collected in a py dict
    """
    with app.test_client() as client:
        response = client.post('/',
                                data={'address1': 'YO32 9GX',
                                'address2': 'YO10 3LF',
                                'address3': 'YO1 7HH',
                                'address4': 'YO1 9TJ',
                                'address5': 'YO24 1AB',
                                'key': 'YO31 8HY'},
                                follow_redirects=True)
        assert response.status_code == 200