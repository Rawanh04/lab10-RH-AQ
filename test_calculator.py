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
        self.assertEqual(substract(3, 2), 1) # 3 - 2 = 1
        self.assertEqual(substract(1, 0), 1) # 1 - 0 = 1
        self.assertEqual(substract(-1, 4), -5) # -1 - 4 = -5
        self.assertEqual(substract(0, -6), 6) # 0 - (-6) = 6
        self.assertEqual(substract(0, 9), -9) # 0 - 9 = -9

    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(20, 1000), 2.3)
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(100, 2), 0.15)

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(-5, ValueError)
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()