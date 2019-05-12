#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @date   : 2019/5/9
# @author : Rong Ya-feng
# @desc   : Chapter 1 : Programming Exercise2

import turtle
'''
# Case Study : ComputeDistanceGraphics
# Prompt the user for inputting two points
x1, y1 = eval(input("Enter x1 and y1 for point 1: "))
x2, y2 = eval(input("Enter x2 and y2 for point 2: "))
distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
turtle.pu()
turtle.goto(x1, y1)
turtle.write("Point 1")
turtle.pd()
turtle.goto(x2, y2)
turtle.write("Point 2")
turtle.pu()
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2)
turtle.write(distance)
turtle.done()
'''

# Draw a rectangle
'''
width, height = eval(input("Enter the width and height of a rectangle:"))
for i in range(2):
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)
turtle.done()
'''

# Draw four hexagons
'''
def drawHexagon():
    turtle.seth(30)
    for i in range(6):
        turtle.fd(40)
        turtle.lt(60)

def drawFourHexagons():
    drawHexagon()
    turtle.pu()
    turtle.goto(0, -80)
    turtle.pd()
    drawHexagon()
    turtle.pu()
    turtle.goto(80, 0)
    turtle.pd()
    drawHexagon()
    turtle.pu()
    turtle.goto(80, -80)
    turtle.pd()
    drawHexagon()
    
if __name__ == '__main__':
    drawFourHexagons()

turtle.done()
'''

# Draw a circle
'''
radius = eval(input("Enter the radius of a circle:"))
PI = 3.1415926
area = radius * radius * PI
turtle.circle(radius)
turtle.pu()
turtle.goto(0, radius)
turtle.pd()
turtle.write(area)
turtle.ht()
turtle.done()
'''
