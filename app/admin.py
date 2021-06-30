import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/register', methods=('GET','POST'))
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        db = get_db()
        error = None # will be used to store errors later

        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'
        # using fetchone() will grab the next row from the result set    
        elif db.execute('SELECT id FROM user WHERE username = ?', (username,)).fetchone() is not None:
            error = f'Username ${username} is already in use'
        
        if error is None:
            db.execute('INSERT INTO user (username, pass_hash) VALUES (?, ?)' (username, generate_password_hash(password)))
            db.commit()
            return redirect(url_for('admin.login'))
        # flash stores a message that can be retrieved when generating the template
        flash(error)    

    return render_template('admin/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        db = get_db()
        error = None
        
        login = db.execute('''SELECT id,pass_hash FROM user WHERE username = ?''', (username,))

        if not username:
            error = 'Incorrect Username'
        elif not check_password_hash(login['password'], password):
            error = 'Incorrect Password'
        
        if error is None:
            session.clear()
            session['user_id'] = login['id']
            return redirect(url_for('index'))
    return render_template('admin/login.html')
        
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute('SELECT * FROM user WHERE id = ?', (user_id,)).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('admin.login'))

        return view(**kwargs)

    return wrapped_view