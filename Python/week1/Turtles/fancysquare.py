import turtle
import sys
sys.setExecutionLimit(35000)

def draw_square(t, sz):
    """Get turtle t to draw a square with sz side"""

    for i in range(1):
        t.forward(sz)
        t.left(90)

def draw_sprite(fancy, legs, length):
    #define angle between legs
    angle = 360 / legs
    #loop over number of legs to draw sprite
    for i in range(legs):
        #move turtle forward
        fancy.forward(length)
        #bring turtle back to start
        fancy.forward(-length)
        #turn turtle by desired angle
        fancy.left(angle)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightblue")

    fancy = turtle.Turtle()
    fancy.color("deeppink")
    fancy.penup()
    fancy.goto(-100,-100)
    fancy.pendown()

    for i in range(4):
        draw_square(fancy,200)
        draw_sprite(fancy, 16, 50)

    wn.exitonclick()

if __name__ == "__main__":
    main()
