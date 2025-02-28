import unittest
from HW4 import closest_pair_dac_start
from HW4_Utils import Point

# 20
class TestClosestPairDAC(unittest.TestCase):

    def test_basic_case(self):
        points = [Point(1, 1), Point(3, 3), Point(6, 6)]
        result = closest_pair_dac_start(points)
        expected = (Point(1, 1), Point(3, 3))  # closest points by distance
        self.assertEqual(result, expected)

    def test_single_point(self):
        points = [Point(1, 1)]
        result = closest_pair_dac_start(points)
        # No pair to compare, should return None or raise an error
        self.assertIsNone(result)  # Or another appropriate behavior

    def test_two_points(self):
        points = [Point(1, 1), Point(4, 5)]
        result = closest_pair_dac_start(points)
        expected = (Point(1, 1), Point(4, 5))
        self.assertEqual(result, expected)

    def test_points_with_zero_coordinates(self):
        points = [Point(0, 0), Point(3, 4), Point(9, 8)]
        result = closest_pair_dac_start(points)
        expected = (Point(0, 0), Point(3, 4))  # Closest points are (0, 0) and (3, 4)
        self.assertEqual(result, expected)

    def test_large_distance(self):
        points = [Point(1, 1), Point(100, 100), Point(200, 200)]
        result = closest_pair_dac_start(points)
        expected = (Point(1, 1), Point(100, 100))  # These two are the closest pair
        self.assertEqual(result, expected)

    def test_edge_case_empty(self):
        points = []
        result = closest_pair_dac_start(points)
        # No points to compare
        self.assertIsNone(result)

    def test_edge_case_two_points_same(self):
        points = [Point(2, 2), Point(2, 2)]
        result = closest_pair_dac_start(points)
        expected = (Point(2, 2), Point(2, 2))  # The closest pair is the same point twice
        self.assertEqual(result, expected)

    def test_closest_pair_5th_and_6th(self):
        # Create 10 points, all with height 2 (y = 2), with varying x values
        points = [
            Point(1, 2),
            Point(3, 2),
            Point(6, 2),
            Point(10, 2),
            Point(15, 2),
            Point(16, 2),  # 5th and 6th points, closest pair
            Point(20, 2),
            Point(30, 2),
            Point(40, 2),
            Point(50, 2)
        ]

        result = closest_pair_dac_start(points)
        expected = (Point(15, 2), Point(16, 2))  # 5th and 6th points are the closest

        self.assertEqual(result, expected)
    
    def test_closest_pair_1st_and_2nd(self):
        # Create 10 points, all with height 2 (y = 2), with varying x values
        points = [
            Point(1, 2),  # 1st and 2nd points, closest pair
            Point(2, 2),
            Point(6, 2),
            Point(10, 2),
            Point(15, 2),
            Point(20, 2),
            Point(30, 2),
            Point(40, 2),
            Point(50, 2),
            Point(60, 2)
        ]

        result = closest_pair_dac_start(points)
        expected = (Point(1, 2), Point(2, 2))  # 1st and 2nd points are the closest

        self.assertEqual(result, expected)
    
    def test_closest_pair_9th_and_10th(self):
        # Create 10 points, all with height 2 (y = 2), with varying x values
        points = [
            Point(1, 10),
            Point(2, 20),
            Point(6, 5),
            Point(10, 20),
            Point(15, 2),
            Point(20, 2),
            Point(30, 2),
            Point(40, 2),
            Point(50, 2),  # 9th and 10th points, closest pair
            Point(51, 2)
        ]

        result = closest_pair_dac_start(points)
        expected = (Point(50, 2), Point(51, 2))  # 9th and 10th points are the closest

        self.assertEqual(result, expected)
