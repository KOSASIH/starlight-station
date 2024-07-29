# Test the main entry point of the StarlightStation project

import unittest
from unittest.mock import patch, MagicMock
from main import main

class TestMain(unittest.TestCase):
    @patch('main.StarlightStation')
    def test_main(self, mock_StarlightStation):
        # Test the main function
        main()
        self.assertTrue(mock_StarlightStation.called)

    def test_main_with_args(self):
        # Test the main function with arguments
        with self.assertRaises(SystemExit):
            main(['--help'])

if __name__ == '__main__':
    unittest.main()
