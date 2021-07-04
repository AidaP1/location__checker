from flask import render_template, Blueprint, request, flash, g, redirect, url_for
from werkzeug.exceptions import abort

from app.admin import login_required
from app.db import get_db
from app.query_gmaps import call_google

bp = Blueprint('index',__name__)

@bp.route('/', methods=["GET", "POST"])
@login_required
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