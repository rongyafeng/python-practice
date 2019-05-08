#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@date   : 2019/5/4
#@author : Rong Ya-feng
import turtle

turtle.screensize(400,300)
turtle.pensize(4) #设置画笔的粗细
turtle.colormode(255) #设置GBK颜色范围为0-255
turtle.color((255,155,192),"pink") #设置画笔颜色和填充颜色
turtle.setup(840,500) #设置主窗口的大小为840*500
turtle.speed(10) #设置画笔速度为10（最快）

# 鼻子
turtle.penup() #提笔
turtle.goto(-100 ,100) # 画笔前往坐标(-100,100)
turtle.pendown() # 下笔
turtle.setheading(-30) # 笔的角度为-30°
turtle.begin_fill() # 外形填充的开始标志
a = 0.4
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.08
        turtle.left(3)  # 向左转3度
        turtle.forward(a)  # 向前走a的步长
    else:
        a = a - 0.08
        turtle.left(3)
        turtle.forward(a)
turtle.end_fill()  # 依据轮廓填充

turtle.penup()  # 提笔
turtle.setheading(90)  # 笔的角度为90度
turtle.forward(25)  # 向前移动25
turtle.setheading(0)  # 转换画笔的角度为0
turtle.forward(10)
turtle.pendown()
turtle.pencolor(255,155,192)  # 设置画笔颜色
turtle.seth(10)
turtle.begin_fill()
turtle.circle(5)  # 画一个半径为5的圆
turtle.color(160,82,45)  # 设置画笔和填充颜色
turtle.end_fill()
turtle.penup()
turtle.setheading(0)
turtle.forward(20)
turtle.pendown()
turtle.pencolor(255,155,192)
turtle.setheading(10)
turtle.begin_fill()
turtle.circle(5)
turtle.color(160,82,45)
turtle.end_fill()

# 头
turtle.color((255,155,192),"pink")
turtle.penup()
turtle.setheading(90)
turtle.forward(41)
turtle.setheading(0)
turtle.forward(0)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(180)
turtle.circle(300,- 30)  # 顺时针画一个半径为300,圆心角为30°的园
turtle.circle(100,- 60)
turtle.circle(80,- 100)
turtle.circle(150,- 20)
turtle.circle(60,- 95)
turtle.setheading(161)
turtle.circle(-300,15)
turtle.penup()
turtle.goto(-100,100)
turtle.pendown()
turtle.setheading(-30)
a = 0.4
for i in range(60):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.08
        turtle.left(3)  # 向左转3度
        turtle.forward(a)  # 向前走a的步长
    else:
        a = a - 0.08
        turtle.left(3)
        turtle.forward(a)
turtle.end_fill()

# 耳朵
turtle.color((255,155,192),"pink")
turtle.penup()
turtle.setheading(90)
turtle.forward(-7)
turtle.setheading(0)
turtle.forward(70)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(100)
turtle.circle(-50,50)
turtle.circle(-10,120)
turtle.circle(-50,54)
turtle.end_fill()
turtle.penup()
turtle.setheading(90)
turtle.forward(-12)
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(100)
turtle.circle(-50,50)
turtle.circle(-10,120)
turtle.circle(-50,56)
turtle.end_fill()

# 眼睛
turtle.color((255,155,192),"white")
turtle.penup()
turtle.setheading(90)
turtle.forward(-20)
turtle.setheading(0)
turtle.forward(-95)
turtle.pendown()
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()
turtle.color("black")
turtle.penup()
turtle.setheading(90)
turtle.forward(12)
turtle.setheading(0)
turtle.forward(-3)
turtle.pendown()
turtle.begin_fill()
turtle.circle(3)
turtle.end_fill()
turtle.color((255,155,192),"white")
turtle.penup()
turtle.setheading(90)
turtle.forward(-25)
turtle.setheading(0)
turtle.forward(40)
turtle.pendown()
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()
turtle.color("black")
turtle.penup()
turtle.setheading(90)
turtle.forward(12)
turtle.setheading(0)
turtle.forward(-3)
turtle.pendown()
turtle.begin_fill()
turtle.circle(3)
turtle.end_fill()

# 腮
turtle.color((255,155,192))
turtle.penup()
turtle.setheading(90)
turtle.forward(-95)
turtle.setheading(0)
turtle.forward(65)
turtle.pendown()
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

# 嘴
turtle.color(239,69,19)
turtle.penup()
turtle.setheading(90)
turtle.forward(15)
turtle.setheading(0)
turtle.forward(-100)
turtle.pendown()
turtle.setheading(-80)
turtle.circle(30,40)
turtle.circle(40,80)

# 身体
turtle.color("red",( 255,99,71))
turtle.penup()
turtle.setheading(90)
turtle.forward(-20)
turtle.setheading(0)
turtle.forward(-78)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(-130)
turtle.circle(100,10)
turtle.circle(300,30)
turtle.setheading(0)
turtle.forward(230)
turtle.setheading(90)
turtle.circle(300,30)
turtle.circle(100,3 )
turtle.color((255,155,192),(255,100,100))
turtle.setheading(-135)
turtle.circle(-80,63)
turtle.circle(-150,24)
turtle.end_fill()

# 手
turtle.color((255,155,192))
turtle.penup()
turtle.setheading(90)
turtle.forward(-40)
turtle.setheading(0)
turtle.forward(-27)
turtle.pendown()
turtle.setheading(-160)
turtle.circle(300,15)
turtle.penup()
turtle.setheading(90)
turtle.forward(15)
turtle.setheading(0)
turtle.forward(0)
turtle.pendown()
turtle.setheading(-10)
turtle.circle(-20,90)
turtle.penup()
turtle.setheading(90)
turtle.forward(30)
turtle.setheading(0)
turtle.forward(237)
turtle.pendown()
turtle.setheading(-20)
turtle.circle(-300,15)
turtle.penup()
turtle.setheading(90)
turtle.forward(20)
turtle.seth(0)
turtle.forward(0)
turtle.pendown()
turtle.setheading(-170)
turtle.circle(20,90)

# 脚
turtle.pensize(10)
turtle.color((240,128,128))
turtle.penup()
turtle.setheading(90)
turtle.forward(-75)
turtle.setheading(0)
turtle.forward(-180)
turtle.pendown()
turtle.setheading(-90)
turtle.forward(40)
turtle.setheading(-180)
turtle.color("black")
turtle.pensize(15)
turtle.forward(20)
turtle.pensize(10)
turtle.color((240,128,128))
turtle.penup()
turtle.setheading(90)
turtle.forward(40)
turtle.setheading(0)
turtle.forward(90)
turtle.pendown()
turtle.setheading(-90)
turtle.forward(40)
turtle.setheading(-180)
turtle.color("black")
turtle.pensize(15)
turtle.forward(20)

# 尾巴
turtle.pensize(4)
turtle.color((255,155,192))
turtle.penup()
turtle.setheading(90)
turtle.forward(70)
turtle.setheading(0)
turtle.forward(95)
turtle.pendown()
turtle.setheading(0)
turtle.circle(70,20)
turtle.circle(10,330)
turtle.circle(70,30)

turtle.done()