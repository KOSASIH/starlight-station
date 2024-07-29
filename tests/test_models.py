# Test the models of the StarlightStation project

import unittest
from unittest.mock import patch, MagicMock
from models.user import User
from models.settings import Settings
from models.data import Data

class TestModels(unittest.TestCase):
    def test_user_model(self):
        # Test the user model
        user = User('test', 'test@example.com')
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'test@example.com')

    def test_settings_model(self):
        # Test the settings model
        settings = Settings('test', 'test_value')
        self.assertEqual(settings.key, 'test')
        self.assertEqual(settings.value, 'test_value')

    def test_data_model(self):
        # Test the data model
        data = Data('test', 'test_data')
        self.assertEqual(data.name, 'test')
        self.assertEqual(data.data, 'test_data')

if __name__ == '__main__':
    unittest.main()
