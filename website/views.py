from flask import Blueprint, render_template, jsonify
from flask_login import login_required
from .models import User

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template('home.html')

@views.route('/debug-user/<email>')
def debug_user(email):
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({
            "id": user.id,
            "email": user.email,
            "fullname": user.fullname,
            "password_hash": user.password
        })
    else:
        return jsonify({"error": "User not found"}), 404
