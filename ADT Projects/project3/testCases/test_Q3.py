import unittest
from HW3 import quick_hull_start, quick_hull
from HW3_Utils import Point

class QuickHullStart(unittest.TestCase):

    def test_quick_hull_start_square(self):
        points = [Point(1, 1), Point(1, 3), Point(3, 1), Point(3, 3)]
        expected = [Point(1, 1), Point(1, 3), Point(3, 1), Point(3, 3)]  # Convex hull of a square
        result = quick_hull_start(points)
        self.assertEqual(sorted(result, key=lambda p: (p.x, p.y)), sorted(expected, key=lambda p: (p.x, p.y)))

    def test_quick_hull_start_triangle(self):
        points = [Point(1, 1), Point(2, 3), Point(3, 1)]
        expected = [Point(1, 1), Point(2, 3), Point(3, 1)]  # Convex hull of a triangle
        result = quick_hull_start(points)
        self.assertEqual(sorted(result, key=lambda p: (p.x, p.y)), sorted(expected, key=lambda p: (p.x, p.y)))

    def test_points_on_the_same_line(self):
        points = [Point(1, 1), Point(2, 2), Point(3, 3)]
        expected = [Point(1, 1), Point(3, 3)]  # Convex hull should be the two outer points
        result = quick_hull_start(points)
        self.assertEqual(sorted(result, key=lambda p: (p.x, p.y)), sorted(expected, key=lambda p: (p.x, p.y)))

    def test_quick_hull_start_with_extra_points_inside(self):
        points = [Point(1, 1), Point(2, 5), Point(3, 1), Point(2, 3), Point(4, 2)]
        expected = [Point(1, 1), Point(2, 5), Point(3, 1), Point(4, 2)]  # Convex hull without the inner point (2, 3)
        result = quick_hull_start(points)
        self.assertEqual(sorted(result, key=lambda p: (p.x, p.y)), sorted(expected, key=lambda p: (p.x, p.y)))

    def test_quick_hull_start_with_duplicate_points(self):
        points = [Point(1, 1), Point(2, 2), Point(2, 2), Point(3, 1)]
        expected = [Point(1, 1), Point(2, 2), Point(3, 1)]  # Convex hull should handle duplicates and return unique points
        result = quick_hull_start(points)
        self.assertEqual(sorted(result, key=lambda p: (p.x, p.y)), sorted(expected, key=lambda p: (p.x, p.y)))

    def test_quick_hull_start_single_point(self):
        points = [Point(1, 1)]
        expected = [Point(1, 1)]  # Single point forms its own convex hull
        result = quick_hull_start(points)
        self.assertEqual(sorted(result, key=lambda p: (p.x, p.y)), sorted(expected, key=lambda p: (p.x, p.y)))

    def test_no_input(self):
        points = []
        expected = []
        result = quick_hull_start(points)
        self.assertEqual(result, expected)

    def test_large_set_of_points(self):
        points = [
            Point(30, 30),
            Point(50, 60),
            Point(60, 20),
            Point(70, 45),
            Point(86, 39),
            Point(112, 60),
            Point(200, 113),
            Point(250, 50),
            Point(300, 200),
            Point(130, 240),
            Point(76, 150),
            Point(47, 76),
            Point(36, 40),
            Point(33, 35),
        ]
        
        expected = [
            Point(60, 20),
            Point(250, 50),
            Point(300, 200),
            Point(130, 240),
            Point(76, 150),
            Point(47, 76),
            Point(30, 30),
        ]
        
        result = quick_hull_start(points)
        
        # Sorting both results for comparison (to handle possible order differences)
        self.assertEqual(sorted(result, key=lambda p: (p.x, p.y)), sorted(expected, key=lambda p: (p.x, p.y)))

    def test_large_set_of_points2(self):
        points = [
            Point(50, 60),
            Point(60, 20),
            Point(70, 45),
            Point(100, 70),
            Point(125, 90),
            Point(200, 113),
            Point(250, 140),
            Point(180, 170),
            Point(105, 140),
            Point(79, 140),
            Point(60, 85),
        ]
        
        expected = [
            Point(60, 20),
            Point(250, 140),
            Point(180, 170),
            Point(79, 140),
            Point(50, 60),
        ]
        
        result = quick_hull_start(points)
        
        # Sorting both results for comparison (to handle possible order differences)
        self.assertEqual(sorted(result, key=lambda p: (p.x, p.y)), sorted(expected, key=lambda p: (p.x, p.y)))

    def test_same_input_output(self):
        points = [
            Point(60, 20),
            Point(250, 140),
            Point(180, 170),
            Point(79, 140),
            Point(50, 60),
        ]
        
        expected = [
            Point(60, 20),
            Point(250, 140),
            Point(180, 170),
            Point(79, 140),
            Point(50, 60),
        ]
        
        result = quick_hull_start(points)
        
        # Sorting both results for comparison (to handle possible order differences)
        self.assertEqual(sorted(result, key=lambda p: (p.x, p.y)), sorted(expected, key=lambda p: (p.x, p.y)))

    def test_convex_hull_two_points(self):
        points = [Point(1, 1), Point(1, 2)]
        expected = [Point(1, 1), Point(1, 2)]
        result = quick_hull_start(points)
        self.assertEqual(sorted(result, key=lambda p: (p.x, p.y)), sorted(expected, key=lambda p: (p.x, p.y)))
