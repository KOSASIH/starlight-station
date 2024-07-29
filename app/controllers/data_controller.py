"""
Data Controller

This controller handles data-related requests.
"""

from flask import Blueprint, request, jsonify
from app.models import Data
from app.utils import get_logger

data_blueprint = Blueprint('data', __name__)

logger = get_logger(__name__)

@data_blueprint.route('/data', methods=['POST'])
def create_data():
    """
    Create a new piece of data.

    Args:
        user_id (int): The ID of the user.
        name (str): The name of the data.
        value (str): The value of the data.

    Returns:
        JSON response with the ID of the new data.
    """
    data = request.get_json()
    user_id = data.get('user_id')
    name = data.get('name')
    value = data.get('value')

    if not user_id or not name or not value:
        return jsonify({'error': 'Invalid request'}), 400

    data = Data(user_id, name, value)
    db.session.add(data)
    db.session.commit()

    return jsonify({'id': data.id}), 201

@data_blueprint.route('/data', methods=['GET'])
def get_data():
    """
    Get a user's data.

    Args:
        user_id (int): The ID of the user.

    Returns:
        JSON response with a list of data.
    """
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'Invalid request'}), 400

    data = Data.query.filter_by(user_id=user_id).all()
    return jsonify([{'id': d.id, 'name': d.name, 'value': d.value} for d in data]), 200

@data_blueprint.route('/data/<int:data_id>', methods=['GET'])
def get_data_by_id(data_id):
    """
    Get a piece of data by ID.

    Args:
        data_id (int): The ID of the data.

    Returns:
        JSON response with the data.
    """
    data = Data.query.get(data_id)
    if not data:
        return jsonify({'error': 'Data not found'}), 404

    return jsonify({'id': data.id, 'name': data.name, 'value': data.value}), 200

@data_blueprint.route('/data/<int:data_id>', methods=['PUT'])
def update_data(data_id):
    """
    Update a piece of data.

    Args:
        data_id (int): The ID of the data.
        name (str): The new name of the data.
        value (str): The new value of the data.

    Returns:
        JSON response with a success message.
    """
    data = request.get_json()
    name = data.get('name')
    value = data.get('value')

    if not name or not value:
        return jsonify({'error': 'Invalid request'}), 400

    data = Data.query.get(data_id)
    if not data:
        return jsonify({'error': 'Data not found'}), 404

    data.name = name
    data.value = value
    db.session.commit()

    return jsonify({'message': 'Data updated successfully'}), 200

@data_blueprint.route('/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    """
    Delete a piece of data.

    Args:
        data_id (int): The ID of the data.

    Returns:
        JSON response with a success message.
    """
    data = Data.query.get(data_id)
    if not data:
        return jsonify({'error': 'Data not found'}), 404

    db.session.delete(data)
    db.session.commit()

    return jsonify({'message': 'Data deleted successfully'}), 200
