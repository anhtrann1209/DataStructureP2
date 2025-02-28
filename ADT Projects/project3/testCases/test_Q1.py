import unittest
from HW3 import left_turn, value_based_on_line_distance
from HW3_Utils import Point

class TestLeftTurn(unittest.TestCase):
    
    # Q1a.1
    def test_left_turn(self):
        a = Point(1, 1)
        b = Point(2, 1)
        i = Point(1, 2)
        self.assertTrue(left_turn(a, b, i))  # Left turn, cross product positive

    # Q1a.2
    def test_right_turn(self):
        a = Point(1, 1)
        b = Point(2, 1)
        i = Point(3, 0)
        self.assertFalse(left_turn(a, b, i))  # Right turn, cross product negative

    # Q1a.3
    def test_collinear(self):
        a = Point(1, 1)
        b = Point(2, 1)
        i = Point(3, 1)
        self.assertFalse(left_turn(a, b, i))  # Collinear, cross product zero

    # Q1a.4
    def test_same_points(self):
        a = Point(2, 3)
        b = Point(2, 3)
        i = Point(2, 3)
        self.assertFalse(left_turn(a, b, i))  # Same points, no turn

    # Q1a.5
    def test_large_coordinates(self):
        a = Point(1000, 1000)
        b = Point(2000, 1000)
        i = Point(1500, 2000)
        self.assertTrue(left_turn(a, b, i))  # Left turn with large coordinates


class TestValueBasedOnLineDistance(unittest.TestCase):

    # Q1b.1
    def test_distance_perpendicular(self):
        a = Point(1, 1)
        b = Point(3, 1)
        p = Point(2, 2)
        # Perpendicular distance from (2, 2) to the line y = 1 is 1
        self.assertEqual(value_based_on_line_distance(a, b, p), 2)

    # Q1b.2
    def test_distance_on_line(self):
        a = Point(1, 1)
        b = Point(3, 3)
        p = Point(2, 2)  # Point (2, 2) is on the line y = x
        self.assertEqual(value_based_on_line_distance(a, b, p), 0)  # Point on the line

    # Q1b.3
    def test_distance_vertical_line(self):
        a = Point(3, 1)
        b = Point(3, 3)
        p = Point(2, 2)  # Vertical line, distance is horizontal distance
        self.assertEqual(value_based_on_line_distance(a, b, p), 2)

    # Q1b.4
    def test_distance_horizontal_line(self):
        a = Point(1, 2)
        b = Point(3, 2)
        p = Point(2, 3)  # Horizontal line, distance is vertical distance
        self.assertEqual(value_based_on_line_distance(a, b, p), 2)

    # Q1b.5
    def test_large_coordinates(self):
        a = Point(1000, 1000)
        b = Point(2000, 1000)
        p = Point(1500, 2000)  # Point is far from the line
        # Perpendicular distance can be calculated using the formula
        expected_distance = 1000000
        self.assertEqual(value_based_on_line_distance(a, b, p), expected_distance)

    # Q1b.6
    def test_same_points(self):
        a = Point(2, 3)
        b = Point(2, 3)
        p = Point(2, 4)  # Same points for a and b, distance is just the distance to the point
        self.assertEqual(value_based_on_line_distance(a, b, p), 0)  # No line, distance is irrelevant (degenerate case)

    # Q1b.7
    def test_vertical_line_and_point_above(self):
        a = Point(1, 1)
        b = Point(1, 3)
        p = Point(2, 2)  # Point (2, 2) is not on the line but vertically away
        self.assertEqual(value_based_on_line_distance(a, b, p), 2)
 