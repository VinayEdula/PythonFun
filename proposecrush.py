import time
import turtle
pen = turtle.Turtle()
turtle.bgcolor("black")
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)
def heart():
    time.sleep(10)
    pen.color("red")
    pen.fillcolor("red")
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()
def txt():
    pen.up()
    pen.setpos(-68, 95)
    pen.down()
    pen.color('white')
    pen.write("I Love You", font=("Verdana", 20, "bold"))
    pen.setpos(-40, 65)
    pen.down()
    pen.color('white')
    pen.write("Kajal", font=("Verdana", 20, "bold"))
    time.sleep(10)
heart()
txt()
pen.ht()
