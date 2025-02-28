import unittest
from HW1 import power_iterative

class TestPowerIterative(unittest.TestCase):

    def test_power_iterative_proper(self):
        """Test cases for proper input"""
        self.assertEqual(power_iterative(2, 3), 8)  # Positive base, positive exponent
        self.assertEqual(power_iterative(5, 0), 1)  # Any base raised to 0 should be 1
        self.assertEqual(power_iterative(1, 5), 1)  # 1 raised to any exponent is 1
        self.assertEqual(power_iterative(0, 3), 0)  # 0 raised to any positive exponent is 0
        self.assertEqual(power_iterative(2, 1), 2)  # Base raised to 1 should be the base
        self.assertEqual(power_iterative(-2, 3), -8)  # Negative base with an odd exponent
        self.assertEqual(power_iterative(-2, 2), 4)  # Negative base with an even exponent

    def test_power_iterative_edge(self):
        """Test cases for edge cases"""
        self.assertEqual(power_iterative(0, 0), 1)  # By convention, 0^0 is defined as 1
        self.assertEqual(power_iterative(-1, 0), 1)  # Any base to the power of 0 is 1

    def test_power_iterative_improper(self):
        """Test cases for improper input"""
        self.assertIsNone(power_iterative("2", 3))  # Base is not a number
        self.assertIsNone(power_iterative(2, "3"))  # Exponent is not a number
        self.assertIsNone(power_iterative(2, -3))  # Negative exponent
        self.assertIsNone(power_iterative(0, -1))  # 0 raised to a negative exponent is undefined
        self.assertIsNone(power_iterative(2, 1.5))  # Exponent is a float