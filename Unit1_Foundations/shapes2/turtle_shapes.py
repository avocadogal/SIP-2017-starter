from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)

### Write your code below:
sides = input("enter number of sides")
angle = 360/sides
for i in range(sides):
    forward(100)
    left(angle)



# Close window on click.
exitonclick()
