#Python turtle to display colourful graphics
import turtle
colors = [ "pink","yellow","blue","green","white","red"]
sketch = turtle.Pen()
turtle.bgcolor("black")
turtle.speed(200)
for i in range(100):
   sketch.pencolor(colors[i % 6])
   sketch.width(i/100 + 1)
   sketch.forward(i)
   sketch.left(59)