from flask import Blueprint, render_template, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    if request.method == 'POST':
        print(data)
    return render_template('login.html', text="This is the Login Page - Test")

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        fullname = request.form.get('fullname')
        password = request.form.get('password') 
        confirm_password = request.form.get('confirm_password')
        
        if len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(fullname) < 6:
            flash('Full name must be greater than 5 characters', category='error')
        elif password != confirm_password:
            flash('Passwords do not match', category='error')
        elif len(password) < 7:
            flash('Password must be at least 6 characters', category='error')
        else:
            new_user = User(email=email, fullname=fullname, password=password)
            flash('Account created!', category='success')

    return render_template('register.html')

@auth.route('/logout')
def logout():
    return "<h1>Logout Page</h1>"