#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @date   : 2019/5/8
# @author : Rong Ya-feng
# @desc   : Chapter 1 : Programming Exercises2

import turtle
# Draw four squares
'''
turtle.penup()
turtle.goto(40, 0)
turtle.pendown()
turtle.fd(40)
turtle.lt(90)
turtle.fd(80)
turtle.lt(90)
turtle.fd(80)
turtle.lt(90)
turtle.fd(80)
turtle.lt(90)
turtle.fd(40)
turtle.pu()
turtle.goto(0, 40)
turtle.pd()
turtle.fd(80)
turtle.pu()
turtle.goto(40, 0)
turtle.pd()
turtle.seth(90)
turtle.fd(80)
turtle.done()
'''

# Draw a cross
'''
turtle.fd(80)
turtle.pu()
turtle.goto(40, 40)
turtle.pd()
turtle.rt(90)
turtle.fd(80)
turtle.done()
'''

# Draw a triangle
'''
turtle.rt(60)
turtle.fd(80)
turtle.rt(120)
turtle.fd(80)
turtle.rt(120)
turtle.fd(80)
turtle.done()
'''

# Draw two triangles
'''
turtle.rt(60)
turtle.fd(80)
turtle.rt(120)
turtle.fd(80)
turtle.rt(120)
turtle.fd(160)
turtle.lt(120)
turtle.fd(80)
turtle.lt(120)
turtle.fd(80)
turtle.done()
'''

# Draw four circles
'''
turtle.circle(40)
turtle.pu()
turtle.goto(0, 80)
turtle.pd()
turtle.circle(40)
turtle.pu()
turtle.goto(80, 80)
turtle.pd()
turtle.circle(40)
turtle.pu()
turtle.goto(80, 0)
turtle.pd()
turtle.circle(40)
turtle.done()
'''

# Draw a line
'''
turtle.pu()
turtle.goto(-39, 49)
turtle.pd()
turtle.write("(-39,49)")
turtle.goto(50, -50)
turtle.write("(50,-50)")
turtle.ht()
turtle.done()
'''

# Draw a star
'''
for i in range(5):
    turtle.fd(100)
    turtle.rt(144)
turtle.done()
'''
# Draw a polygon
'''
turtle.pu()
turtle.goto(40, -69.28)
turtle.pd()
turtle.goto(-40, -69.28)
turtle.goto(-80, -9.8)
turtle.goto(-40, 69)
turtle.goto(40, 69)
turtle.goto(80, 0)
turtle.goto(40, -69.28)
turtle.ht()
turtle.done()
'''

# Display a rectanguloid
'''
turtle.goto(200, 0)
turtle.goto(200, 100)
turtle.goto(0, 100)
turtle.goto(0, 0)
turtle.pu()
turtle.goto(50, 50)
turtle.pd()
turtle.goto(250, 50)
turtle.goto(250, 150)
turtle.goto(50, 150)
turtle.goto(50, 50)
turtle.goto(0, 0)
turtle.pu()
turtle.goto(0, 100)
turtle.pd()
turtle.goto(50, 150)
turtle.pu()
turtle.goto(250, 150)
turtle.pd()
turtle.goto(200, 100)
turtle.pu()
turtle.goto(250, 50)
turtle.pd()
turtle.goto(200, 0)
turtle.done()
'''

# Display a clock
'''
turtle.circle(106)
turtle.pu()
turtle.goto(100, 100)
turtle.pd()
turtle.write("3", align = "center")
turtle.pu()
turtle.goto(0, 0)
turtle.pd()
turtle.write("6", align = "center")
turtle.pu()
turtle.goto(-100, 100)
turtle.pd()
turtle.write("9", align = "center")
turtle.pu()
turtle.goto(0, 198)
turtle.pd()
turtle.write("12", align = "center")
turtle.pensize(3)
turtle.pu()
turtle.goto(0, 106)
turtle.pd()
turtle.goto(-45, 106)
turtle.pensize(2)
turtle.pu()
turtle.goto(0, 106)
turtle.pd()
turtle.goto(55, 106)
turtle.pensize(1)
turtle.pu()
turtle.goto(0, 106)
turtle.pd()
turtle.goto(0, 176)
turtle.pu()
turtle.goto(0, -15)
turtle.pd()
turtle.write("9:15:00", align = "center")
turtle.ht()
turtle.done()
'''
