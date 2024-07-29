# -*- coding: utf-8 -*-

"""
Data Model

This model represents a piece of data in the application.
"""

from app import db
from app.utils import get_logger

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    value = db.Column(db.String(128), nullable=False)

    def __init__(self, user_id, name, value):
        self.user_id = user_id
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Data('{self.user_id}', '{self.name}', '{self.value}')"
