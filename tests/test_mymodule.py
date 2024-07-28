# coding: utf-8
import unittest
import math
from mypackage import mymodule

class MyModuleTest(unittest.TestCase):
    def test_calc_pi(self):
        area = mymodule.calc_pi(100)
        print(area)
        self.assertEqual(area, math.pi * 100 ** 2, "π * r^2 is the area of the circle")

    def test_calc_e(self):
        area = mymodule.calc_e(100)
        print(area)  
        self.assertEqual(area, math.e * 100 ** 2, "e is the base of the natural logarithm")
