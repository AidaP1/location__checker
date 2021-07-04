from flask import render_template, Blueprint, request, flash, g, redirect, url_for, session
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

@bp.route('/locations', methods=["GET", "POST"])
@login_required
def locations():
    user_id = session.get('user_id')
    db = get_db()
    if request.method == "POST":
        loc_name = request.form.get('new-loc-name')
        loc_adr = request.form.get('new-loc-adr')
        error = None

        if not loc_name:
            error = 'You must enter a location name'
        elif not loc_adr:
            error = 'You must enter a location address'
        elif db.execute('''SELECT user.id FROM user
                            JOIN location ON user.id = location.user_id
                            WHERE user.id = ? AND location.name = ?''', (user_id, loc_name,)).fetchone() is not None:
            error = 'You already have a location with that name'
        elif db.execute('''SELECT user.id FROM user
                            JOIN location ON user.id = location.user_id
                            WHERE user.id = ? AND location.address = ?''', (user_id, loc_adr,)).fetchone() is not None:
            error = 'You already have that location saved'
        
        if error == None:
            db.execute('INSERT INTO location (user_id, name, address) VALUES (?, ?, ?)', (user_id, loc_name, loc_adr,))
            db.commit()
    
    
    locations = db.execute('''SELECT user.id, name, address FROM user
                                JOIN location ON user.id = location.user_id
                                WHERE user.id = ?''', (user_id,)).fetchall()
    return render_template('locations.html', locations=locations)