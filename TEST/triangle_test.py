import unittest

from triangle import *

class GeometryTests(unittest.TestCase):

    def test_area_triangle_positive(self):
        res = AreaTriangle(6, 8)
        self.assertEqual(res, 24)

    def test_area_triangle_zero(self):
        res = AreaTriangle(0, 5)
        self.assertEqual(res, 0)

    def test_area_triangle_negative(self):
        res = AreaTriangle(-4, 6)
        self.assertEqual(res, -12)

    def test_perimeter_triangle_positive(self):
        res = PerimeterTriangle(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_triangle_zero(self):
        res = PerimeterTriangle(0, 4, 5)
        self.assertEqual(res, 9)

    def test_perimeter_triangle_negative(self):
        res = PerimeterTriangle(-3, 4, 5)
        self.assertEqual(res, 6)
