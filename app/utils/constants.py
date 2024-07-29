# -*- coding: utf-8 -*-

"""
Constants Module

This module contains various constants for the application.
"""

import os

# Environment variables
ENV_VAR_LOG_LEVEL = "LOG_LEVEL"
ENV_VAR_DB_HOST = "DB_HOST"
ENV_VAR_DB_PORT = "DB_PORT"
ENV_VAR_DB_USERNAME = "DB_USERNAME"
ENV_VAR_DB_PASSWORD = "DB_PASSWORD"

# Logging levels
LOG_LEVEL_INFO = "INFO"
LOG_LEVEL_DEBUG = "DEBUG"
LOG_LEVEL_WARNING = "WARNING"
LOG_LEVEL_ERROR = "ERROR"
LOG_LEVEL_CRITICAL = "CRITICAL"

# Database settings
DB_HOST = os.environ.get(ENV_VAR_DB_HOST, "localhost")
DB_PORT = int(os.environ.get(ENV_VAR_DB_PORT, 5432))
DB_USERNAME = os.environ.get(ENV_VAR_DB_USERNAME, "username")
DB_PASSWORD = os.environ.get(ENV_VAR_DB_PASSWORD, "password")

# API settings
API_HOST = "localhost"
API_PORT = 8000
API_VERSION = "v1"
