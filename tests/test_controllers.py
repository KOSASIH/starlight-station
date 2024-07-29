# Test the controllers of the StarlightStation project

import unittest
from unittest.mock import patch, MagicMock
from controllers.user_controller import UserController
from controllers.settings_controller import SettingsController
from controllers.data_controller import DataController

class TestControllers(unittest.TestCase):
    def test_user_controller(self):
        # Test the user controller
        user_controller = UserController()
        result = user_controller.get_users()
        self.assertIsNotNone(result)

    def test_settings_controller(self):
        # Test the settings controller
        settings_controller = SettingsController()
        result = settings_controller.get_settings()
        self.assertIsNotNone(result)

    def test_data_controller(self):
        # Test the data controller
        data_controller = DataController()
        result = data_controller.get_data()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
