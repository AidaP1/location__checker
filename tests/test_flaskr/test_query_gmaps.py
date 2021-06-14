"""
This file (test_query_gmaps.py) contains the unit tests for the query_gmaps.py file.
"""

from werkzeug.wrappers import response
from app.query_gmaps import call_google

def test_call_google_five_loc():
    """
    GIVEN a set of 5 addresses and a key location
    WHEN the google maps API is called
    THEN check the response is valid
    """
    query = {'address1': 'YO32 9GX',
            'address2': 'YO10 3LF',
            'address3': 'YO1 7HH',
            'address4': 'YO1 9TJ',
            'address5': 'YO24 1AB',
            'key': 'YO31 8HY'}

    data = call_google(query)
    assert data != None
    