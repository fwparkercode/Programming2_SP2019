from turtle import *

my_turtle = Turtle()
my_window = Screen()

my_turtle.goto(0, 0)
# my_turtle.goto(100,100)

my_turtle.fillcolor('red')

my_window.colormode(255)
for j in range(20):
    my_turtle.begin_fill()
    my_turtle.left(20)
    for i in range(3):
        my_turtle.fillcolor((255, j * 12, j * 12))
        my_turtle.right(120)
        my_turtle.forward(10 * j)
    my_turtle.end_fill()

my_window.exitonclick()
