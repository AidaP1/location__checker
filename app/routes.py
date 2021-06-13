from flask import render_template, redirect, request
from werkzeug.wrappers import response

from app import app


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = {'address1': request.form.get('address1'),
                'address2': request.form.get('address2'),
                'address3': request.form.get('address3'),
                'address4': request.form.get('address4'),
                'address5': request.form.get('address5'),
                'key': request.form.get('key')}
    
        output = call_google(query)


        return render_template("success.html", output=output)
    return render_template('index.html')