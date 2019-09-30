import turtle
import random

#for randcolor in ["darkred", "red", "redorange", "orange",
#           "yelloworange", "yellow", "yellowgreen",
#           "green", "aquamarine", "blue", "darkblue",
#           "purple", "magenta", "hotpink", "pink"]:

wn = turtle.Screen()
vanessa = turtle.Turtle()
vanessa.shape("turtle")

vanessa.penup()
vanessa.forward(-150)
vanessa.pendown()

# triangle
vanessa.color("black", "red")
vanessa.begin_fill()
for loop in range(3):
    vanessa.left(120)
    vanessa.forward(50)
vanessa.end_fill()

vanessa.penup()
vanessa.forward(75)
vanessa.pendown()

# square
vanessa.color("black", "orange")
vanessa.begin_fill()
for loop in range(4):
    vanessa.left(90)
    vanessa.forward(50)
vanessa.end_fill()

vanessa.penup()
vanessa.forward(85)
vanessa.pendown()

# hexagon
vanessa.color("black", "yellow")
vanessa.begin_fill()
for loop in range(6):
    vanessa.left(60)
    vanessa.forward(50)
vanessa.end_fill()

vanessa.penup()
vanessa.forward(125)
vanessa.pendown()

# octagon
vanessa.color("black", "green")
vanessa.begin_fill()
for loop in range(8):
    vanessa.left(45)
    vanessa.forward(50)
vanessa.end_fill()

wn.exitonclick()
