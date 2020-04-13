'''
Project: Draw Flower 2-3 CIS 210 Winter 2019
Author: Derek Martin
Credits: N/A

Use Python to create a design or drawing
'''

from turtle import *

def drawFlower(numSquares):
    '''
    (int) -> graphics

    calls drawPolygon function to create a flower-like object using Turtle graphics
    '''
    rotate = 360 / numSquares #rotate after each square to achieve flower shape
    for i in range(numSquares):
        drawPolygon(25, 4)
        right(rotate)
    return None

def drawPolygon(sideLength, numSides):
    '''
    (number), (int) -> graphics

    draws a polygon with Turtle graphics using given side length and number of sides
    '''
    turnAngle = 360 / numSides #used to rotate the pen to draw each side of a polygon
    for i in range(numSides):
        forward(sideLength)
        right(turnAngle)
    return None

def main():
    '''
    used to execute the program
    '''
    drawFlower(25)
    return None

left(90)
forward(50)
main()
