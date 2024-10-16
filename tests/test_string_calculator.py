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

    # Step 6: Custom delimiters
    def test_custom_delimiters(self):
        self.assertEqual(self.calculator.add("//;\n1;2"), 3)
        self.assertEqual(self.calculator.add("//|\n2|3|4"), 9)

    # Step 7: Negative numbers throw exception
    def test_negative_numbers_throw_exception(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-2,3")
        self.assertEqual(str(context.exception), "negative numbers not allowed: -2")

        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-2,-3")
        self.assertEqual(str(context.exception), "negative numbers not allowed: -2,-3")

    # Step 8: Ignore numbers grater than 1000000
    def test_ignore_numbers_greater_than_1000000(self):
        self.assertEqual(self.calculator.add("2,1000001,6"), 8)
        self.assertEqual(self.calculator.add("1000,999,1000010"), 1999)

    # Step 9: Ignore white space around numbers
    def test_whitespace_handling(self):
        self.assertEqual(self.calculator.add(" 1 , 2 "), 3)
        self.assertEqual(self.calculator.add(" 3\n4 "), 7)

#    Step 10: Return 0 for input with only delimiters
    def test_only_delimiters(self):
        self.assertEqual(self.calculator.add(",\n"), 0)
        self.assertEqual(self.calculator.add(",,,\n"), 0)
