import requests
import os


def call_API(query):
    try:
        # build a google maps directions matrix api call
        api_key = os.environ.get("API_KEY")
        url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={query['key']}&destinations="
        # varies with the number of locations user wants to check
        for key in query:
            if 'key' not in key:
                url = url + f"{query[key]}|"
        url = url.rstrip(str(-1)) + f"&key={api_key}"
        
        response = requests.get(url)
        # gather json
        trips = response.json()
        response.raise_for_status()
    except requests.RequestException:
        return None
    return trips

def format_response(trips, query):
    # turn the json into a dict of dicts with relevant info
    try:
        output = []
        keys = []
        i = 1

        for key in query:
            keys.append(key)
        
        for trip in trips['rows'][0]['elements']:
            item = {
                'name': keys[i],
                'time': trip['duration']['text'],
                'distance': trip['distance']['text']
            }
            output.append(item)
            i += 1
        return output
    except:
        return None

# give 1 function to be called in the main app
def call_google(query):
    api_response = call_API(query)
    return format_response(api_response, query)
