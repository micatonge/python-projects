from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = -250
y_pos = -150
# t.setposition(x_pos, y_pos)

### Write your code below:
pendown()
# pen color
for x in range(4):
    forward(100)
    right(90)

penup()


pendown()
for x in range(3):
     forward(100)
     right(120)
