from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
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
            new_user = User(email=email, fullname=fullname, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template('register.html')

@auth.route('/logout')
def logout():
    return "<h1>Logout Page</h1>"

@auth.route('/delete_user/<email>')
def delete_user(email):
    user = User.query.filter_by(email=email).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return f"User {email} deleted."
    return "User not found."