# -*- coding: utf-8 -*-

"""
Settings Model

This model represents a user's settings in the application.
"""

from app import db
from app.utils import get_logger

class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    theme = db.Column(db.String(64), nullable=False, default='light')
    language = db.Column(db.String(64), nullable=False, default='en')
    notifications = db.Column(db.Boolean, nullable=False, default=True)

    def __init__(self, user_id, theme, language, notifications):
        self.user_id = user_id
        self.theme = theme
        self.language = language
        self.notifications = notifications

    def __repr__(self):
        return f"Settings('{self.user_id}', '{self.theme}', '{self.language}', '{self.notifications}')"
