# -*- coding: utf-8 -*-

"""
Notification Service

This service provides notification-related functionality.
"""

import logging
from typing import Optional

from app.models import Notification
from app.utils import get_logger

class NotificationService:
    def __init__(self):
        self.logger = get_logger(__name__)

    def send_notification(self, notification: Notification) -> bool:
        """
        Send a notification.

        Args:
            notification (Notification): The notification to send.

        Returns:
            bool: True if sent successfully, otherwise False.
        """
        try:
            # Send the notification using a notification library or API
            return True
        except Exception as e:
            self.logger.error(f"Error sending notification: {e}")
            return False

        def get_notifications(self, user_id: int) -> Optional[list]:
        """
        Get notifications for a user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            Optional[list]: A list of notifications for the user, or None if no notifications are found.
        """
        try:
            notifications = Notification.query.filter_by(user_id=user_id).all()
            return notifications
        except Exception as e:
            self.logger.error(f"Error getting notifications: {e}")
            return None

    def mark_notification_as_read(self, notification_id: int) -> bool:
        """
        Mark a notification as read.

        Args:
            notification_id (int): The ID of the notification.

        Returns:
            bool: True if the notification was marked as read successfully, otherwise False.
        """
        try:
            notification = Notification.query.get(notification_id)
            if notification:
                notification.read = True
                notification.save()
                return True
            return False
        except Exception as e:
            self.logger.error(f"Error marking notification as read: {e}")
            return False

    def delete_notification(self, notification_id: int) -> bool:
        """
        Delete a notification.

        Args:
            notification_id (int): The ID of the notification.

        Returns:
            bool: True if the notification was deleted successfully, otherwise False.
        """
        try:
            notification = Notification.query.get(notification_id)
            if notification:
                notification.delete()
                return True
            return False
        except Exception as e:
            self.logger.error(f"Error deleting notification: {e}")
            return False
