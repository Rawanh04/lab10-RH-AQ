#https://github.com/Rawanh04/lab10-RH-AQ
#Partner 1: Rawan Hussain
#Partner 2: Ashley Quintana

import math
"""
Link:
Partner 1: Rawan Hussain
Partner 2: Ashley Quintana

calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a ,b):
    if a == 0:
        return ZeroDivisionError
    else:
        return b / a

def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return math.pow(a, b)

def multiply(a, b):
    return a * b

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError
    return math.log(b, a)

def exponent(a,b):
    return a**b

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)


