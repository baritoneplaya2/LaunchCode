import random
import turtle
wn = turtle.Screen()
pirate = turtle.Turtle()
pirate.shape("turtle")
pirate.speed(4)
pirate.color("black")

pirate_angle = random.randrange(-360, 360)
pirate.left(pirate_angle)
pirate.forward(100)
pirate.left(pirate_angle)
pirate.forward(100)
pirate.left(pirate_angle)
pirate.forward(100)
data = [160, -43, 270, -97, -43, 200, -940, 17, -86]
for angle in data:
    pirate.left(angle)
    pirate.forward(100)
