# -*- coding: utf-8 -*-

"""
Data Service

This service provides data-related functionality.
"""

import logging
from typing import Optional

from app.models import Data
from app.utils import get_logger

class DataService:
    def __init__(self):
        self.logger = get_logger(__name__)

    def get_data(self, id: int) -> Optional[Data]:
        """
        Get data by ID.

        Args:
            id (int): The ID of the data.

        Returns:
            Optional[Data]: The data if found, otherwise None.
        """
        try:
            data = Data.query.get(id)
            return data
        except Exception as e:
            self.logger.error(f"Error getting data: {e}")
            return None

    def create_data(self, data: Data) -> bool:
        """
        Create new data.

        Args:
            data (Data): The data to create.

        Returns:
            bool: True if created successfully, otherwise False.
        """
        try:
            data.save()
            return True
        except Exception as e:
            self.logger.error(f"Error creating data: {e}")
            return False

    def update_data(self, id: int, data: Data) -> bool:
        """
        Update existing data.

        Args:
            id (int): The ID of the data.
            data (Data): The updated data.

        Returns:
            bool: True if updated successfully, otherwise False.
        """
        try:
            existing_data = Data.query.get(id)
            if existing_data:
                existing_data.update(data)
                return True
            return False
        except Exception as e:
            self.logger.error(f"Error updating data: {e}")
            return False

    def delete_data(self, id: int) -> bool:
        """
        Delete data by ID.

        Args:
            id (int): The ID of the data.

        Returns:
            bool: True if deleted successfully, otherwise False.
        """
        try:
            data = Data.query.get(id)
            if data:
                data.delete()
                return True
            return False
        except Exception as e:
            self.logger.error(f"Error deleting data: {e}")
            return False
