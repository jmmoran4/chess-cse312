import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
import db
import db

bp = Blueprint('auth', __name__, url_prefix='/auth')


# File needs work, need to handle user exist, user not exist, and incorrect username/password
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        mydb = db

    @bp.route('/login', methods=('GET', 'POST'))
    def login():
        return render_template('auth/login.html')

    return render_template('auth/register.html')