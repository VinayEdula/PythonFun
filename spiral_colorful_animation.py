import turtle
rainbow = turtle.Turtle()
rainbow.speed(0)
rainbow.hideturtle()
turtle.bgcolor("black")
colors = ["red", "orange", "yellow", "green",
          "blue", "purple"]
rainbow.penup()
rainbow.setposition(-300, 0)
rainbow.pendown()
for i in range(360):
    rainbow.pencolor(colors[i % 6])
    rainbow.width(i/100+1)
    rainbow.forward(i)
    rainbow.left(59)
turtle.down()
