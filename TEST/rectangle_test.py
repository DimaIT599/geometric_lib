import unittest

from rectangle import *

class RecnangleTests(unittest.TestCase):

    def test_area_positive(self):
        res = area(3, 4)
        self.assertEqual(res, 12)

    def test_area_zero(self):
        res = area(0, 5)
        self.assertEqual(res, 0)

    def test_area_negative(self):
        res = area(-2, 3)
        self.assertEqual(res, -6)

    def test_perimeter_positive(self):
        res = perimeter(3, 4)
        self.assertEqual(res, 14)

    def test_perimeter_zero(self):
        res = perimeter(0, 5)
        self.assertEqual(res, 10)

    def test_perimeter_negative(self):
        res = perimeter(-2, 3)
        self.assertEqual(res, 2)

