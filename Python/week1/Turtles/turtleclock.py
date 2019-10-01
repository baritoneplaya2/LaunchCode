import turtle
wn = turtle.Screen()
clock = turtle.Turtle()
clock.speed(10)
clock.shape("turtle")
clock.color("blue")
clock.pensize(3)
wn.bgcolor("lightgreen")
clock.up()
clock.left(60)

for i in range(12):
    clock.forward(170)
    clock.stamp()
    clock.forward(-170)
    clock.right(30)
    
for i in range(12):
    clock.forward(150)
    clock.down()
    clock.forward(-20)
    clock.up()
    clock.forward(-130)
    clock.right(30)

clock.right(60)
wn.exitonclick()
