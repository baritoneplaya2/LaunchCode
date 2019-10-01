import turtle
import sys
sys.setExecutionLimit(35000)

wn = turtle.Screen()
paint = turtle.Turtle()
paint.speed(20)
paint.shape("turtle")
wn.bgcolor("lightblue")
paint.up()

paint.goto(-200,-40)
paint.color("darkblue")
paint.down()

for i in range(30):
    paint.forward(400)
    paint.right(90)
    paint.forward(2)
    paint.right(90)
    paint.forward(400)
    paint.left(90)
    paint.forward(2)
    paint.left(90)

paint.color("tan")
for i in range(10):
    paint.forward(400)
    paint.right(90)
    paint.forward(2)
    paint.right(90)
    paint.forward(400)
    paint.left(90)
    paint.forward(2)
    paint.left(90)
    
paint.up()
paint.goto(120,120)
paint.color("yellow")
for i in range(24):
    paint.forward(50)
    paint.down()
    paint.forward(-50)
    paint.right(15)
    
paint.right(7.5)
for i in range(48):
    paint.forward(40)
    paint.down()
    paint.forward(-40)
    paint.right(7.5)

paint.color("orange")
paint.right(3.25)
for i in range(48):
    paint.forward(25)
    paint.down()
    paint.forward(-25)
    paint.right(7.5)

paint.up()
paint.goto(-120,-120)
paint.color("lightgreen")
wn.exitonclick()
