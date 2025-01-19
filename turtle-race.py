from turtle import Turtle, Screen
import random

screen = Screen()
screen.listen()
screen.setup(width=560, height=350)
user_choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race (Red, Blue, Green, Yellow,"
                                                             "Orange, Purple)? Enter a color:").lower()

colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
y_position = [75, 45, 15, -15, -45, -75]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-270, y_position[turtle_index])
    all_turtles.append(new_turtle)


is_race_on = False
if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 260:
            winning_color = turtle.pencolor()
            if turtle.color() == user_choice:
                print(f"You've won! The {winning_color} turtle is the winner!")
                is_race_on = False
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")
                is_race_on = False
        else:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

screen.exitonclick()
