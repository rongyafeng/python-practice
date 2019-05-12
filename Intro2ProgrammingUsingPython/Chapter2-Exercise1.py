#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @date   : 2019/5/10
# @author : Rong Ya-feng
# @desc   : Chapter 1 : Programming Exercise1

# Case Study:Display the current time(GMT)

"""
import time
currentTime = time.time()
# obtain the total seconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime)
currentSecond = totalSeconds % 60
totalMinutes = totalSeconds // 60
currentMinute = totalMinutes % 60
totalHours = totalMinutes // 60
currentHour = totalHours % 24
print("Current time is", currentHour, ":", currentMinute, ":", currentSecond, "GMT")
"""

# Case Study:Computing distance
'''
# Prompt the user for inputting two points
x1, y1 = eval(input("Enter x1 and y1 for point 1: "))
x2, y2 = eval(input("Enter x2 and y2 for point 2: "))
distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
print("The distance between the two points is", distance)
'''

# Convert Celsius to Fahrenheit
'''
celsius = eval(input("Input a degree in Celsius:"))
fahrenheit = (9 / 5) * celsius + 32
print(celsius, "Celsius is", fahrenheit, "Fahrenheit")
'''

# Compute the volume of a cylinder
'''
radius, length = eval(input("Enter the radius and length of a cylinder:"))
PI = 3.1415926
area = radius * radius * PI
volume = area * length
print("The area is", area)
print("The volume is", volume)
'''

# Convert feet into meters# Financial application : calculate tips
'''
feet = eval(input("Enter a value for feet:"))
meters = feet * 0.305
print(feet, "feet is", meters, "meters")
'''

# Convert pounds into kilograms
'''
pounds = eval(input("Enter a value in pounds:"))
kilograms = pounds * 0.454
print(pounds, "pounds is", kilograms, "kilograms")
'''

# Calculate tips
'''
subtotal, gratuityRate = eval(input("Enter the subtotal and a gratuity rate:"))
gratuity = subtotal * gratuityRate
total = subtotal + gratuity
print("The gratuity is",gratuity, "and the total is ", total)
'''

# Sum the digits in an integer
'''
digits = eval(input("Enter a number between 0 and 1000:"))
singleDigits = digits % 10
hundredsDigit = digits // 100
tenDigit = (digits // 10) - (hundredsDigit * 10)
sum = hundredsDigit + tenDigit + singleDigits
print("The sum of the digits is",sum)
'''

# Find the number of years and days
'''
minutes = eval(input("Enter the number of minutes:"))
years = minutes // 525600
resMinutes = minutes % 525600
days = resMinutes // 1440
print(minutes, "minutes is approximately", years, "years and",days, "days" )
'''
# Calculate energy
'''
waterAmount = eval(input("Enter the amount of water in kilograms:"))
initialTemperature = eval(input("Enter the initial temperature:"))
finalTemperature = eval(input("Enter the al temperature:"))
energy = waterAmount * (finalTemperature - initialTemperature) * 4184
print("The energy needed is", energy) 
'''

# Wind chill temperature
'''
outsideTemperature = eval(input("Enter the temperature in Fahrenheit between -58 and 41:"))
windSpeed = eval(input("Enter the wind speed in miles per hour:"))
windChill = 35.74 + 0.6215 * outsideTemperature - 35.75 * windSpeed ** 0.16 + \
            0.4275 * outsideTemperature * windSpeed ** 0.16
print("The wind chill index is", windChill)
'''

# Find runway length
'''
speed, acceleration = eval(input("Enter speed and acceleration:"))
runwayLength = speed**2 / 2 * acceleration
print("The mimium runway length for this plane is", runwayLength, "meters")
'''

# Print a table
'''
print("a    b    a ** b")
x = 1
for i in range(5):
    print(x, "   ", x+1, "   ", x ** (x + 1))
'''

# Split digits
'''
digit = eval(input("Enter an integer:"))
a3 = digit // 1000
a2 = digit % 1000 // 100
a1 = digit % 1000 % 100 // 10
a0 = digit % 1000 % 100 % 10
print(a3, a2, a1, a0)
'''

# Area of a triangle
'''
x1, y1, x2, y2, x3, y3 = eval(input("Enter three points of a triangle:"))
side1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
side2 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
side3 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
s = (side1 + side2 + side3) / 2
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
print("The area of the triangle is", area)
'''

# Area of a hexagon
'''
side = eval(input("Enter the side:"))
area = (3 * 3 ** 0.5 * side ** 2 ) / 2
print("The area of the hexagon is", area)
'''