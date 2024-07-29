# Test the utility functions of the StarlightStation project

import unittest
from unittest.mock import patch, MagicMock
from utils.helpers import *
from utils.decorators import *
from utils.constants import *

class TestUtils(unittest.TestCase):
    def test_helper_function(self):
        # Test a helper function
        result = helper_function('test')
        self.assertEqual(result, 'test_helper')

    def test_decorator(self):
        # Test a decorator
        @my_decorator
        def test_function():
            return 'test'
        result = test_function()
        self.assertEqual(result, 'test_decorated')

    def test_constant(self):
        # Test a constant
        self.assertEqual(MY_CONSTANT, 'y_constant')

if __name__ == '__main__':
    unittest.main()
