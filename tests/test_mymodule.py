# coding: utf-8

import unittest
import math
from mypackage import mymodule

class MyModuleTest(unittest.TestCase):
    def test_calc(self):
        area = mymodule.calc(2)
        self.assertEqual(area, math.pi, "the area of ??the unit circle is π")
        