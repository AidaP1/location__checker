"""
This file (test_query_gmaps.py) contains the unit tests for the query_gmaps.py file.
"""

from werkzeug.wrappers import response
from app.query_gmaps import call_google, call_API, format_response

def test_call_API_5_loc():
    """
    GIVEN a set of 5 locations and a key value
    WHEN the google maps API is called
    THEN receive a successful response
    """
    query = {'address1': 'YO32 9GX',
            'address2': 'YO10 3LF',
            'address3': 'YO1 7HH',
            'address4': 'YO1 9TJ',
            'address5': 'YO24 1AB',
            'key': 'YO31 8HY'}
    data = call_API(query)
    assert data['status'] =='OK'

def test_call_API_4_loc():
    """
    GIVEN a set of 4 locations and a key value
    WHEN the google maps API is called
    THEN receive a successful response
    """
    query = {'address1': 'YO32 9GX',
            'address2': 'YO10 3LF',
            'address3': 'YO1 7HH',
            'address4': 'YO1 9TJ',
            'key': 'YO31 8HY'}
    data = call_API(query)
    assert data['status'] =='OK'

def test_call_API_3_loc():
    """
    GIVEN a set of 3 locations and a key value
    WHEN the google maps API is called
    THEN receive a successful response
    """
    query = {'address1': 'YO32 9GX',
            'address2': 'YO10 3LF',
            'address3': 'YO1 7HH',
            'key': 'YO31 8HY'}
    data = call_API(query)
    assert data['status'] =='OK'

def test_call_API_2_loc():
    """
    GIVEN a set of 2 locations and a key value
    WHEN the google maps API is called
    THEN receive a successful response
    """
    query = {'address1': 'YO32 9GX',
            'address2': 'YO10 3LF',
            'key': 'YO31 8HY'}
    data = call_API(query)
    assert data['status'] =='OK'

def test_call_API_1_loc():
    """
    GIVEN a set of 1 locations and a key value
    WHEN the google maps API is called
    THEN receive a successful response
    """
    query = {'address1': 'YO32 9GX',
            'key': 'YO31 8HY'}
    data = call_API(query)
    assert data['status'] =='OK'

def test_call_google_5_loc():
    """
    GIVEN a set of 5 addresses and a key location
    WHEN the google maps API is called
    THEN check the response is formatted and can be used on-site
    """
    query = {'address1': 'YO32 9GX',
            'address2': 'YO10 3LF',
            'address3': 'YO1 7HH',
            'address4': 'YO1 9TJ',
            'address5': 'YO24 1AB',
            'key': 'YO31 8HY'}

    data = call_google(query)
    assert data != None
    assert data['address1'] != None
    assert data['address2'] != None
    assert data['address3'] != None
    assert data['address4'] != None
    assert data['address5'] != None
    
