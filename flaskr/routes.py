import urllib.parse
import requests
import os

from flask import render_template, redirect, request
from werkzeug.wrappers import response

from flaskr import app

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = {'address1': request.form.get('address1'),
                'address2': request.form.get('address2'),
                'address3': request.form.get('address3'),
                'address4': request.form.get('address4'),
                'address5': request.form.get('address5'),
                'key': request.form.get('key')}
        try:
            api_key = os.environ.get("API_KEY")
            url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={query['key']}&destinations={query['address1']}|{query['address2']}|{query['address3']}|{query['address4']}|{query['address5']}&key={api_key}"
            response = requests.get(url)
            trips = response.json()
            response.raise_for_status()
        except requests.RequestException:
            print('API failed')
            return None

        output = {
        }
        i = 1
        
        for trip in trips['rows'][0]['elements']:
            key = 'address' + str(i)
            value = trip['duration']['text']
            output[key] = value
            i += 1



        return render_template("success.html", output=output, trips=trips)
    return render_template('index.html')