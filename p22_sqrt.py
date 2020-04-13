'''
Project 2.2 CIS 210 Winter 2019
Author: Derek Martin
Credits: N/A

Write 3 functions that calculate, compare, and print the square root of an input using different methods.
'''
import math
def mysqrt(n, k):
    '''
    (int), (int) -> float

    Given inputs n and k, calculate the square root of n using a formula, k number of times. Return the result (square root of n)
    
    >>> mysqrt(100, 10)
    10.0
    >>> mysqrt(25, 10)
    5.0
    '''
    n = abs(n) #Converts n to a positive number
    x = 1
    sqrt = None #Returns 'None' if k = 0
    for i in range(k):
        sqrt = (0.5 * (x + (n/x)))
        x = sqrt
    return sqrt

def sqrt_compare(num, iterations):
    '''
    (number), (int) -> string

    Call the mysqrt function using given parameters as inputs, then compare results with imported math library sqrt function. Print the results and the calculated percent error value.

    >>> sqrt_compare(10000, 8)
    For 10000 using 8 iterations:
    mysqrt value is: 101.20218365353946
    math lib sqrt value is: 100.0
    This is a 1.2 percent error.
    '''
    test = mysqrt(num, iterations)
    approximate_result = math.sqrt(num) #This is approximate because it's using 'sqrt' from the imported math module
    difference = abs(round((((approximate_result - test) / approximate_result) * 100), 2))
    print("For", num, "using", iterations, "iterations:")
    print("mysqrt value is:", test)
    print("math lib sqrt value is:", approximate_result)
    print("This is a", difference, "percent error.")
    return None

def main():
    '''Square root comparison program driver'''
    sqrt_compare(25, 5)
    sqrt_compare(25, 10)
    sqrt_compare(625, 5)
    sqrt_compare(625, 10)
    sqrt_compare(10000, 8)
    sqrt_compare(10000, 10)
    sqrt_compare(10000, 11)
    return None

main()
