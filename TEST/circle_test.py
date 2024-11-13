import unittest
import math
from circle import *



class RectangleClassTest(unittest.TestCase):
    
    def test_Perimetr_one(self):
        res = PerimeterCircle(1)
        self.assertEqual(res, 1 * 2 * math.pi)
    
    def test_Perimetr_two_float(self):
        res = PerimeterCircle(2.01)
        self.assertAlmostEqual(res, 2 * 2.01 * math.pi)
    
    def test_Perimetr_minus_one(self):
        res = PerimeterCircle(-1)
        self.assertEqual(res, -1 * 2 * math.pi)
    
    def test_Area_three(self):
        res = AreaCircle(-3)
        self.assertEqual(res, -3 * -3 * math.pi)
    
    def test_perimeter_circle_zero(self):
        res = PerimeterCircle(0)
        self.assertEqual(res, 1)
        
    def test_Area_fife(self):
        res = AreaCircle(1.01)
        self.assertAlmostEqual(res, 1.01 * 1.01 * math.pi)
