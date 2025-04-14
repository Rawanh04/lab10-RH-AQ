#https://github.com/Rawanh04/lab10-RH-AQ
#Partner 1: Rawan Hussain
#Partner 2: Ashley Quintana

import unittest
from calculator import *
# Link:
# Partner 1: Rawan Hussain
# Partner 2: Ashley Quintana

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5) # 2 + 3 = 5
        self.assertEqual(add(0, 1), 1) # 0 + 1 = 1
        self.assertEqual(add(-1, -5), -6) # -1 + (-5) = -6
        self.assertEqual(add(3, 0), 3) # 3 + 0 = 3

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(3, 2), 1) # 3 - 2 = 1
        self.assertEqual(subtract(1, 0), 1) # 1 - 0 = 1
        self.assertEqual(subtract(-1, 4), -5) # -1 - 4 = -5
        self.assertEqual(subtract(0, -6), 6) # 0 - (-6) = 6
        self.assertEqual(subtract(0, 9), -9) # 0 - 9 = -9

    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(2, 2), 4)
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(2, 0), 0)
        self.assertNotEqual(multiply(5, 0), 5)
        self.assertNotEqual(multiply(5, 1), -5)
        self.assertEqual(multiply(2, -1), -2)
        self.assertEqual(multiply(-1,-1),1)
        self.assertEqual(multiply(0.5,0.5),0.25)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,2), 1)
        self.assertEqual(div(2,3), 1.5)
        self.assertEqual(div(2,0), 0)
        self.assertNotEqual(div(5,0), 5)
        self.assertEqual(div(-1,5),-5)
        self.assertEqual(div(-1,-5),5)
        self.assertEqual(div(10000,1),0.0001)
        self.assertNotEqual(div(10000,-1),1)
        self.assertAlmostEqual(div(3,2),0.6666666666666666)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
            raise ZeroDivisionError


    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(20, 1000), 2.3058653605207224)
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(100, 2), 0.15051499783199057)

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(-5, ValueError)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 5)
            logarithm(5,0)
            logarithm(-5,0)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(2,2), 2.8284271247461903)
        self.assertEqual(hypotenuse(2,0), 2)
        self.assertAlmostEqual(hypotenuse(-2,1), 2.36)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        with self.assertRaises(ValueError):
           square_root(-1)
        # Test basic function
        self.assertEqual(square_root(1), 1)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(0), 0)
    #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()