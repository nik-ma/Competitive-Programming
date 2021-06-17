import turtle
import time
turtle.speed(5)
turtle.bgcolor("white")

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.color("red", "pink")        

turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
curve()
turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()
# turtle.write((100,100),True)
turtle.goto(70,100)
turtle.write("I love you Ankita", True, align="center")

