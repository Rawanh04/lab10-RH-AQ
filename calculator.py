import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b):
    return a+b

def substract(a, b):
    return a-b

def multiply(a, b):
    return a * b

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        raise ZeroDivisionError

def logarithm(a, b):
    try:
        return math.log(b,a)
    except ValueError:
        raise ValueError

def exponent(a,b):
    return a**b
