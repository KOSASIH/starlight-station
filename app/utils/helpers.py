# -*- coding: utf-8 -*-

"""
Helpers Module

This module contains various helper functions for the application.
"""

import logging
import os
import sys
from typing import Optional

import requests

def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance.

    Args:
        name (str): The name of the logger.

    Returns:
        logging.Logger: The logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger

def get_env_var(name: str, default: Optional[str] = None) -> str:
    """
    Get an environment variable.

    Args:
        name (str): The name of the environment variable.
        default (Optional[str]): The default value if the variable is not set.

    Returns:
        str: The value of the environment variable.
    """
    return os.environ.get(name, default)

def send_request(url: str, method: str, data: Optional[dict] = None) -> requests.Response:
    """
    Send a request.

    Args:
        url (str): The URL of the request.
        method (str): The method of the request (e.g., GET, POST, PUT, DELETE).
        data (Optional[dict]): The data to send with the request.

    Returns:
        requests.Response: The response from the request.
    """
    if method.upper() == "GET":
        return requests.get(url, params=data)
    elif method.upper() == "POST":
        return requests.post(url, json=data)
    elif method.upper() == "PUT":
        return requests.put(url, json=data)
    elif method.upper() == "DELETE":
        return requests.delete(url, params=data)
    else:
        raise ValueError("Invalid method")
