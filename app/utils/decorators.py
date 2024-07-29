# -*- coding: utf-8 -*-

"""
Decorators Module

This module contains various decorators for the application.
"""

import logging
import time
from typing import Optional

def timer(func):
    """
    Timer decorator.

    Args:
        func: The function to decorate.

    Returns:
        The decorated function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"Function {func.__name__} took {end_time - start_time} seconds to execute")
        return result
    return wrapper

def retry(max_retries: int = 3, delay: float = 1.0):
    """
    Retry decorator.

    Args:
        max_retries (int): The maximum number of retries.
        delay (float): The delay between retries.

    Returns:
        The decorated function.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logging.error(f"Error occurred: {e}")
                    time.sleep(delay)
            raise Exception("Maximum retries exceeded")
        return wrapper
    return decorator

def singleton(cls):
    """
    Singleton decorator.

    Args:
        cls: The class to decorate.

    Returns:
        The decorated class.
    """
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper
