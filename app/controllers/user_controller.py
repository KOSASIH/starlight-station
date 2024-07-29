# -*- coding: utf-8 -*-

"""
User Controller

This controller handles user-related requests.
"""

from flask import Blueprint, request, jsonify
from app.models import User
from app.utils import get_logger

user_blueprint = Blueprint('user', __name__)

logger = get_logger(__name__)

@user_blueprint.route('/register', methods=['POST'])
def register():
    """
    Register a new user.

    Args:
        username (str): The username of the user.
        email (str): The email of the user.
        password (str): The password of the user.

    Returns:
        JSON response with the user's ID and a success message.
    """
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Invalid request'}), 400

    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({'error': 'User already exists'}), 400

    user = User(username, email, password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'id': user.id, 'essage': 'User created successfully'}), 201

@user_blueprint.route('/login', methods=['POST'])
def login():
    """
    Login a user.

    Args:
        email (str): The email of the user.
        password (str): The password of the user.

    Returns:
        JSON response with the user's ID and a success message.
    """
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Invalid request'}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({'error': 'Invalid credentials'}), 401

    return jsonify({'id': user.id, 'essage': 'User logged in successfully'}), 200

@user_blueprint.route('/users', methods=['GET'])
def get_users():
    """
    Get all users.

    Returns:
        JSON response with a list of users.
    """
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users]), 200
