import unittest
from HW2 import insertion_sort

class TestInsertionSort(unittest.TestCase):
    
    def test_insertion_sort(self):
        # Test cases for proper input
        self.assertEqual(insertion_sort([3, 1, 2]), [1, 2, 3]) # Basic case with unsorted integers
        self.assertEqual(insertion_sort([1, 2, 3]), [1, 2, 3]) # Already sorted list
        self.assertEqual(insertion_sort([3, 2, 1]), [1, 2, 3]) # Reverse sorted list
        self.assertEqual(insertion_sort([5]), [5]) # Single-element list
        self.assertEqual(insertion_sort([]), []) # Empty list
        self.assertEqual(insertion_sort([4, 4, 4]), [4, 4, 4]) # All elements are the same
        self.assertEqual(insertion_sort([3, 1, 2, 2, 1]), [1, 1, 2, 2, 3]) # Duplicates in the list
        self.assertEqual(insertion_sort([-3, -1, -2]), [-3, -2, -1]) # Negative integers 
        self.assertEqual(insertion_sort([1.1, 1.0, 1.2]), [1.0, 1.1, 1.2]) # Floating-point numbers
        self.assertEqual(insertion_sort([4,7,1,3]), [1,3,4,7]) # List of even length
        self.assertEqual(insertion_sort([100, 10, 1000, 0, -10, 50]), [-10, 0, 10, 50, 100, 1000]) # Mixed positive/negative integers

        # Test cases with longer lists
        self.assertEqual(insertion_sort([i for i in range(100, 0, -1)]), [i for i in range(1, 101)]) # Reverse sorted list of length 100
        self.assertEqual(insertion_sort([0.1 * i for i in range(1000, 0, -1)]), [0.1 * i for i in range(1, 1001)]) # Reverse sorted floats

        # Test cases for improper input (assert returns None)
        self.assertIsNone(insertion_sort("not a list")) # Input is not a list
        self.assertIsNone(insertion_sort(None)) # Input is None
        self.assertIsNone(insertion_sort([1, "a", 2])) # List contains non-numeric elements
        self.assertIsNone(insertion_sort([1, None, 3])) # List contains None
        self.assertIsNone(insertion_sort([1, [2], 3])) # List contains nested list             

