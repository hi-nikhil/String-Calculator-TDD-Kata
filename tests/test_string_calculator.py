import unittest
from src.string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = StringCalculator()

    # Step 1: Empty string returns 0
    def test_empty_string_returns_zero(self):
        self.assertEqual(self.calculator.add(""), 0)

    # Step 2: Single number returns itself
    def test_single_number_returns_itself(self):
        self.assertEqual(self.calculator.add("1"), 1)
        self.assertEqual(self.calculator.add("5"), 5)

    # Step 3: Two comma-separated numbers
    def test_two_numbers_comma_separated(self):
        self.assertEqual(self.calculator.add("1,2"), 3)
        self.assertEqual(self.calculator.add("4,5"), 9)

    # Step 4: Multiple comma-separated numbers
    def test_multiple_comma_separated_numbers(self):
        self.assertEqual(self.calculator.add("1,2,3"), 6)
        self.assertEqual(self.calculator.add("5,7,8,2"), 22)

    # Step 5: Newline between numbers
    def test_newline_between_numbers(self):
        self.assertEqual(self.calculator.add("1\n2,3"), 6)
        self.assertEqual(self.calculator.add("4\n5\n6"), 15)
