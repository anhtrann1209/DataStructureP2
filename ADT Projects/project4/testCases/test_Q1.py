import unittest
import math
from HW4 import distance_between
from HW4_Utils import Point

# 2
class TestDistanceFunction(unittest.TestCase):
    def test_basic_case(self):
        # Two points at (0, 0) and (3, 4)
        point1 = Point(0, 0)
        point2 = Point(3, 4)
        result = distance_between(point1, point2)
        expected = 5  # 3-4-5 triangle, distance_between should be 5
        self.assertEqual(result, expected)

    def test_same_point(self):
        # Two points at the same position (2, 2)
        point1 = Point(2, 2)
        point2 = Point(2, 2)
        result = distance_between(point1, point2)
        expected = 0  # Same point, distance_between should be 0
        self.assertEqual(result, expected)

    def test_vertical_distance_between(self):
        # Points with same x but different y
        point1 = Point(1, 1)
        point2 = Point(1, 5)
        result = distance_between(point1, point2)
        expected = 4  # Vertical distance_between
        self.assertEqual(result, expected)

    def test_horizontal_distance_between(self):
        # Points with same y but different x
        point1 = Point(2, 3)
        point2 = Point(5, 3)
        result = distance_between(point1, point2)
        expected = 3  # Horizontal distance_between
        self.assertEqual(result, expected)