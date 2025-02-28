import unittest
from HW2 import merge

class TestMerge(unittest.TestCase):
    
    def merge_test_helper(self, A, p, q, r):
        merge(A, p, q, r)
        return A

    def test_merge(self):
        # Test cases for proper input, even length
        self.assertEqual(self.merge_test_helper([1, 3, 2, 4], 0, 1, 3), [1, 2, 3, 4])
        self.assertEqual(self.merge_test_helper([1, 2, 3, 4], 0, 1, 3), [1, 2, 3, 4])
        self.assertEqual(self.merge_test_helper([3, 4, 1, 2], 0, 1, 3), [1, 2, 3, 4])
        self.assertEqual(self.merge_test_helper([1, 3, 5, 2, 4, 6], 0, 2, 5), [1, 2, 3, 4, 5, 6])
        self.assertEqual(self.merge_test_helper([1, 2, 3, 0, 0, 0], 0, 2, 5), [0, 0, 0, 1, 2, 3])
        self.assertEqual(self.merge_test_helper([0, 0, 0, 1, 2, 3], 0, 2, 5), [0, 0, 0, 1, 2, 3])

        # Test cases for proper input, odd length
        self.assertEqual(self.merge_test_helper([1, 3, 5, 2, 4], 0, 2, 4), [1, 2, 3, 4, 5])
        self.assertEqual(self.merge_test_helper([7, 8, 9, 2, 3], 0, 2, 4), [2, 3, 7, 8, 9])
        self.assertEqual(self.merge_test_helper([1, 2, 3], 0, 1, 2), [1, 2, 3])
        self.assertEqual(self.merge_test_helper([4, 6, 8, 10, 11, -1, 3, 5, 9], 0, 4, 8), [-1, 3, 4, 5, 6, 8, 9, 10, 11])

        # Test cases for proper input, duplicates
        self.assertEqual(self.merge_test_helper([1, 1, 2, 2], 0, 1, 3), [1, 1, 2, 2])
        self.assertEqual(self.merge_test_helper([2, 2, 1, 1], 0, 1, 3), [1, 1, 2, 2])
        self.assertEqual(self.merge_test_helper([1, 2, 3, 4, 1, 2, 3], 0, 3, 6), [1, 1, 2, 2, 3, 3, 4])

        # Test cases for edge cases
        self.assertEqual(self.merge_test_helper([1, 2], 0, 0, 1), [1, 2])
        self.assertEqual(self.merge_test_helper([2, 1], 0, 0, 1), [1, 2])
        self.assertEqual(self.merge_test_helper([1], 0, 0, 0), [1])

