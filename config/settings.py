# -*- coding: utf-8 -*-

"""
Settings Module

This module contains application settings.
"""

import os

# Application settings
APP_NAME = 'Super Advanced High-Tech App'
APP_VERSION = '1.0.0'
APP_ENV = os.environ.get('APP_ENV', 'development')

# Database settings
DB_HOST = 'localhost'
DB_PORT = 5432
DB_USERNAME = 'uperuser'
DB_PASSWORD = 'uperpassword'
DB_NAME = 'uperdatabase'

# API settings
API_HOST = '0.0.0.0'
API_PORT = 5000
API_DEBUG = True

# Security settings
SECRET_KEY = 'upersecretkey'
JWT_SECRET_KEY = 'uperjwtsecretkey'
JWT_TOKEN_EXPIRATION = 3600

# Logging settings
LOG_LEVEL = 'DEBUG'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

# Other settings
CACHE_TTL = 3600
RATE_LIMIT = 100
