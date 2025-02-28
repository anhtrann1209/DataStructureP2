import unittest
from HW1 import polynomial_brute_force

class TestPolynomialBruteForce(unittest.TestCase):

    def test_polynomial_brute_force_proper(self):
        """Test cases for proper input"""
        self.assertEqual(polynomial_brute_force([1, 2, 3], 2), 17)  # P(x) = 1 + 2x + 3x^2, P(2) = 17
        self.assertEqual(polynomial_brute_force([0, 0, 1], 3), 9)  # P(x) = x^2, P(3) = 9
        self.assertEqual(polynomial_brute_force([1], 5), 1)  # P(x) = 1 (constant polynomial)
        self.assertEqual(polynomial_brute_force([], 2), 0)  # Empty coefficients, P(x) = 0
        self.assertEqual(polynomial_brute_force([0, 0, 0], 2), 0) # All zero coefficients
        self.assertEqual(polynomial_brute_force([1, -2, 1], 3), 4)  # P(x) = 1 - 2x + x^2, P(3) = 4

    def test_polynomial_brute_force_edge(self):
        """Test cases for edge cases"""
        self.assertEqual(polynomial_brute_force([1], 0), 1)  # Constant polynomial at x = 0
        self.assertEqual(polynomial_brute_force([1, 0, 0], 0), 1) # P(x) = 1 + 0x + 0x^2, P(0) = 1
        self.assertEqual(polynomial_brute_force([1, 1, 1], -1), 1)  # P(x) = 1 + x + x^2, P(-1) = 1

    def test_polynomial_brute_force_improper(self):
        """Test cases for improper input (assert returns None)"""
        self.assertIsNone(polynomial_brute_force("not a list", 2))  # Coefficients not a list
        self.assertIsNone(polynomial_brute_force([1, 2, 3], "not a number"))  # x is not numeric
        self.assertIsNone(polynomial_brute_force(None, 2))  # Coefficients are None
        self.assertIsNone(polynomial_brute_force([1, 2, "three"], 2))  # Non-numeric coefficient in list
        self.assertIsNone(polynomial_brute_force([1, 2, 3], None))  # x is None