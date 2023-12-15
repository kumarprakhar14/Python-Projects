import turtle
import time

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.penup()

# Set the background color
t.bgcolor("#FFFFFF")

# Draw the virus body
t.pendown()
t.fillcolor("#FF0000")
t.begin_fill()
t.circle(50)
t.end_fill()

# Draw the spikes
for i in range(8):
    t.penup()
    t.goto(50 * t.cos(i * 45), 50 * t.sin(i * 45))
    t.pendown()
    t.forward(20)
    t.backward(10)
    t.left(45)
    t.forward(10)
    t.backward(20)
    t.right(45)

# Draw the eyes
t.penup()
t.goto(20, 20)
t.pendown()
t.fillcolor("#000000")
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.goto(-20, -20)
t.pendown()
t.fillcolor("#000000")
t.begin_fill()
t.circle(5)
t.end_fill()

# Hide the turtle
t.hideturtle()

# Keep the window open until it is closed
time.sleep(10000)
