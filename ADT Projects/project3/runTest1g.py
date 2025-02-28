import unittest
import math
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

def value_based_on_line_distance(a: Point, b: Point, p: Point) -> float:
    """
    Calculates the perpendicular distance from point p to the line defined by points a and b.
    """
    if a.x == b.x and a.y == b.y:
      return math.sqrt((p.x - a.x) ** 2 + (p.y - a.y) ** 2)

    if a.x == b.x:
      return abs(p.x - a.x)  

    if a.y == b.y:
      return abs(p.y - a.y)  

    numerator = abs((b.y - a.y) * p.x - (b.x - a.x) * p.y + (b.x * a.y - b.y * a.x))
    denominator = math.sqrt((b.y - a.y) ** 2 + (b.x - a.x) ** 2)

    return numerator / denominator



class TestValueBasedOnLineDistance(unittest.TestCase):
    def test_distance_perpendicular(self):
        a = Point(0, 0)
        b = Point(4, 0)
        p = Point(2, 2)
        self.assertEqual(value_based_on_line_distance(a, b, p), 2)

    def test_distance_vertical_line(self):
        a = Point(2, 0)
        b = Point(2, 4)
        p = Point(4, 2)
        self.assertEqual(value_based_on_line_distance(a, b, p), 2)

    def test_distance_horizontal_line(self):
        a = Point(0, 2)
        b = Point(4, 2)
        p = Point(2, 0)
        self.assertEqual(value_based_on_line_distance(a, b, p), 2)

    def test_vertical_line_and_point_above(self):
        a = Point(2, 2)
        b = Point(2, 5)
        p = Point(4, 4)
        self.assertEqual(value_based_on_line_distance(a, b, p), 2)

# Run the tests
if __name__ == "__main__":
    unittest.main()
