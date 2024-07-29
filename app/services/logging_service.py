# -*- coding: utf-8 -*-

"""
Logging Service

This service provides logging-related functionality.
"""

import logging
from typing import Optional

from app.utils import get_logger

class LoggingService:
    def __init__(self):
        self.logger = get_logger(__name__)

    def log_info(self, message: str) -> None:
        """
        Log an info message.

        Args:
            message (str): The message to log.
        """
        self.logger.info(message)

    def log_debug(self, message: str) -> None:
        """
        Log a debug message.

        Args:
            message (str): The message to log.
        """
        self.logger.debug(message)

    def log_warning(self, message: str) -> None:
        """
        Log a warning message.

        Args:
            message (str): The message to log.
        """
        self.logger.warning(message)

    def log_error(self, message: str) -> None:
        """
        Log an error message.

        Args:
            message (str): The message to log.
        """
        self.logger.error(message)

    def log_critical(self, message: str) -> None:
        """
        Log a critical message.

        Args:
            message (str): The message to log.
        """
        self.logger.critical(message)
