import unittest
from src.string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = StringCalculator()

    # Step 1: Empty string returns 0
    def test_empty_string_returns_zero(self):
        self.assertEqual(self.calculator.add(""), 0)
