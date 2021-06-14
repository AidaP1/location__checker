import requests
import os


def call_API(query):
    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={query['key']}&destinations={query['address1']}|{query['address2']}|{query['address3']}|{query['address4']}|{query['address5']}&key={api_key}"
        response = requests.get(url)
        trips = response.json()
        response.raise_for_status()
    except requests.RequestException:
        return None
    return trips

def format_response(trips):
    output = {
    }
    i = 1
    
    for trip in trips['rows'][0]['elements']:
        key = 'address' + str(i)
        value = trip['duration']['text']
        output[key] = value
        i += 1
    
    return output

def call_google(query):
    api_response = call_API(query)
    return format_response(api_response)


    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={query['key']}&destinations={query['address1']}|{query['address2']}|{query['address3']}|{query['address4']}|{query['address5']}&key={api_key}"
        response = requests.get(url)
        trips = response.json()
        response.raise_for_status()
    except requests.RequestException:
        return None

    output = {
    }
    i = 1
    
    for trip in trips['rows'][0]['elements']:
        key = 'address' + str(i)
        value = trip['duration']['text']
        output[key] = value
        i += 1
    
    return output