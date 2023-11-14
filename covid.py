#Python turtle to for coronavirus graphics.

from turtle import *
color('white')
bgcolor('black')
speed(100)
hideturtle()
b = 0
while b < 200:
 right(b)
 forward(b * 2)
 b += 1
