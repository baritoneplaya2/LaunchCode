import turtle

wn = turtle.Screen()

def draw_star(t):
    for i in range(5):
        t.forward(100)
        t.left(216) # 216 = 180/5 + 180, but 720/5 also works

def main():
    star = turtle.Turtle()
    wn.bgcolor("lightgreen")
    star.speed(5)
    star.shape("none")
    star.color("hotpink")
    star.pensize(4)
    star.speed(20)
    star.up()
    star.goto(-180,50)
    star.down()
    
    for i in range(5):
        draw_star(star)
        star.up()
        star.forward(350)
        star.right(144)
        star.down()

if __name__ == "__main__":
    main()
