# Test the services of the StarlightStation project

import unittest
from unittest.mock import patch, MagicMock
from services.data_service import DataService
from services.logging_service import LoggingService
from services.notification_service import NotificationService

class TestServices(unittest.TestCase):
    def test_data_service(self):
        # Test the data service
        data_service = DataService()
        result = data_service.get_data()
        self.assertIsNotNone(result)

    def test_logging_service(self):
        # Test the logging service
        logging_service = LoggingService()
        logging_service.log('test')
        self.assertTrue(logging_service.logger.called)

    def test_notification_service(self):
        # Test the notification service
        notification_service = NotificationService()
        notification_service.send_notification('test')
        self.assertTrue(notification_service.notifier.called)

if __name__ == '__main__':
    unittest.main()
