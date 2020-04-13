'''
Project: Determining Net Pay 2-1 CIS 210 Winter 2019
Author: Derek Martin
Credit: N/A

Write functions used to determine net pay after tax calculation and deduction.
'''
def tax(gross_pay):
    '''
    (number) -> float

    Calculate and return the tax amount given gross pay. 15% of gross pay = tax

    >>> tax(100)
    15.0
    >>> tax(200)
    30.0
    '''
    tax = gross_pay * 0.15
    return tax

def netpay(hours):
    '''
    (int) -> float

    Determine the net pay after working a given number of hours.

    >>> netpay(10)
    91.38
    >>> netpay(40)
    365.5
    '''
    gross_pay = hours * 10.75
    netpay = round((gross_pay - tax(gross_pay)), 2)
    return netpay

def main():
    '''Net pay program driver'''
    print("For 10 hours work, netpay is: ", netpay(10))
    print("For 40 hours work, netpay is: ", netpay(40))
    return None

main()
