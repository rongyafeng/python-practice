#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @date   : 2019/5/8
# @author : Rong Ya-feng
# @desc   : Chapter 1 : Programming Exercises1

# Display three different messages
print("Welcome to Python.")
print("Welcome to Computer science.")
print("Programming is fun.")
# Display the same message five times
for i in range(5):
    print("Welcome to Python")
# Display a pattern
print("FFFFFFF  U     U  NN     NN")
print("FF       U     U  NNN    NN")
print("FFFFFFF  U     U  NN N   NN")
print("FF        U   U   NN  N  NN")
print("FF         UUU    NN    NNN")
# Print a table
print("a    a^2    a^3")
a = 0
for i in range(4):
    a = a + 1
    print(a, "   ", a*a, "   ", a*a*a)
# Compute Expressions
print((9.5 * 4.5 - 2.5 * 3) / (45.5 - 3.5))
# Summation of a series
i = 1
sum = 0
for i in range(9):
    sum = sum + i
print("sum = ", sum)
# Approximate pai
print("pai = ", 4 * (1 - 1 / 3 + 1 / 5 - 1 / 7 + 1 / 9 - 1 / 11))
print("pai = ", 4 * (1 - 1 / 3 + 1 / 5 - 1 / 7 + 1 / 9 - 1 / 11 + 1 / 13 - 1 / 15))
print("pai = ", 4 * (1 - 1 / 3 + 1 / 5 - 1 / 7 + 1 / 9 - 1 / 11 + 1 / 13 - 1 / 15 + 1 / 17 - 1 / 19))
# Area and  perimeter of a circle
pai = 3.1415926
radius = 5.5
area = radius * radius * pai
perimeter = 2 * radius * pai
print("area = ", area)
print("perimeter = ", perimeter)
# Area and  perimeter of a rectangle
width = 4.5
height = 7.9
area = width * height
perimeter = 2 * (width + height)
print("area = ", area)
print("perimeter = ", perimeter)
# Average speed
kilometers = 14
minutes = 45
seconds = 30
miles = kilometers / 1.6
hour = (minutes * 60 + seconds) / 3600
averSpeed = miles / hour
print("averSpeed = ", averSpeed)
# Population projection
seconds = 5 * 365 * 24 * 60 * 60
birth = seconds // 7
death = seconds // 13
newImmigrant = seconds // 45
print("birth = ", birth)
print("death = ", death)
print("newImmigrant = ", newImmigrant)