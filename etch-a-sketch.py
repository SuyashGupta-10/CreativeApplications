from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed("fastest")


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def right():
    tim.right(10)


def left():
    tim.left(10)


def clear():
    tim.penup()
    tim.goto(0,0)
    tim.setheading(0)
    tim.clear()
    tim.pendown()


screen.listen()
screen.onkey(fun=forward, key="w")
screen.onkey(fun=left, key="a")
screen.onkey(fun=backward, key="s")
screen.onkey(fun=right, key="d")
screen.onkey(fun=clear, key="c")

screen.exitonclick()