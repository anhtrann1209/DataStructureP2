import unittest
from HW2 import merge_sort

class TestMergeSort(unittest.TestCase):

    # Helper function to simplify merge_sort testing
    def merge_sort_helper(self, A):
        merge_sort(A, 0, len(A) - 1)
        print(A)
        return A

    def test_merge_sort(self):
        # Test cases for proper input
        self.assertEqual(self.merge_sort_helper([3, 1, 2]), [1, 2, 3])  # Basic case with unsorted integers
        self.assertEqual(self.merge_sort_helper([1, 2, 3]), [1, 2, 3])  # Already sorted list
        self.assertEqual(self.merge_sort_helper([3, 2, 1]), [1, 2, 3])  # Reverse sorted list
        self.assertEqual(self.merge_sort_helper([5]), [5])  # Single-element list
        self.assertEqual(self.merge_sort_helper([]), [])  # Empty list
        self.assertEqual(self.merge_sort_helper([4, 4, 4]), [4, 4, 4])  # All elements are the same
        self.assertEqual(self.merge_sort_helper([3, 1, 2, 2, 1]), [1, 1, 2, 2, 3])  # Duplicates in the list
        self.assertEqual(self.merge_sort_helper([-3, -1, -2]), [-3, -2, -1])  # Negative integers
        self.assertEqual(self.merge_sort_helper([1.1, 1.0, 1.2]), [1.0, 1.1, 1.2])  # Floating-point numbers
        self.assertEqual(self.merge_sort_helper([4,7,1,3]), [1,3,4,7])  # List of even length
        self.assertEqual(self.merge_sort_helper([100, 10, 1000, 0, -10, 50]), [-10, 0, 10, 50, 100, 1000])  # Mixed positive/negative integers
 
        # Test cases with longer lists
        self.assertEqual(self.merge_sort_helper([i for i in range(100, 0, -1)]), [i for i in range(1, 101)])  # Reverse sorted list of length 100
        self.assertEqual(self.merge_sort_helper([0.1 * i for i in range(1000, 0, -1)]), [0.1 * i for i in range(1, 1001)])  # Reverse sorted floats      
