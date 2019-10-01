import turtle
import sys

sys.setExecutionLimit(35000)

def draw_spiral(t, angle):
    ''' takes a turtle, t, and an angle in degrees '''
    length = 1
    for i in range(84):
        t.forward(length)
        t.right(angle)
        length = length + 2

def main():
    wn = turtle.Screen()       # Set up the window and its attributes
    wn.bgcolor("lightgreen")

    guido = turtle.Turtle()    # create guido
    guido.color('blue')
    guido.speed(10)

    ## draw the first spiral ##
    # position guido
    guido.penup()
    guido.backward(110)
    guido.pendown()

    # draw the spiral using a 90 degree turn angle
    draw_spiral(guido, 90)
    guido.stamp()

    ## draw the second spiral ##
    # position guido
    guido.penup()
    guido.home()
    guido.forward(90)
    guido.pendown()

    draw_spiral(guido, 89)

if __name__ == "__main__":
    main()
