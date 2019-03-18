import turtle
import random

my_turtle = turtle.Turtle()
my_turtle.speed(6)
my_turtle.width(3)
my_turtle.shape("turtle")
my_screen = turtle.Screen()

'''
my_turtle.goto(0, 0)  # move the turtle to coordinates
my_turtle.goto(100, 0)
my_turtle.goto(100, 100)

my_turtle.pencolor("lightblue")
my_turtle.forward(100)  # driving the turtle
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.right(45)
my_turtle.backward(50)

my_turtle.penup()
my_turtle.goto(0, 0)
my_turtle.pendown()

my_turtle.setheading(90)  # turn to the heading (0 right, 90 up, 180 left)

# draw a shape
my_turtle.fillcolor("red")
my_turtle.pencolor("black")

my_turtle.begin_fill()

for i in range(8):
    my_turtle.forward(50)
    my_turtle.right(360 / 8)

my_turtle.end_fill()


distance = 20
for i in range(500):
    my_turtle.forward(distance)
    my_turtle.right(i)

'''



def rect(width, height):
    '''
    Draws a rectangle to the center of the screen
    :param width:
    :param height:
    :return:
    '''
    my_turtle.penup()
    my_turtle.goto(-width / 2, height / 2)
    my_turtle.pendown()
    my_turtle.pencolor("red")
    my_turtle.setheading(0)
    for i in range(2):
        my_turtle.forward(width)
        my_turtle.right(90)
        my_turtle.forward(height)
        my_turtle.right(90)


def rect_recursive(width, height, depth, line_width=3):
    if depth > 0:
        my_turtle.pensize(line_width)
        my_turtle.penup()
        my_turtle.goto(-width / 2, height / 2)
        my_turtle.pendown()
        my_turtle.pencolor("red")
        my_turtle.setheading(0)
        for i in range(2):
            my_turtle.forward(width)
            my_turtle.right(90)
            my_turtle.forward(height)
            my_turtle.right(90)
        rect_recursive(width * 1.2, height * 1.2, depth - 1, line_width * 1.2)


def bracket_recursion(x, y, size, depth):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(90)
    my_turtle.forward(size)
    my_turtle.right(90)
    my_turtle.forward(100)  # make this constant
    pos1 = my_turtle.pos()

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(270)
    my_turtle.forward(size)
    my_turtle.left(90)
    my_turtle.forward(100)
    pos2 = my_turtle.pos()

    if depth > 0:
        x, y = pos1
        bracket_recursion(x, y, size * 0.5, depth - 1)
        x, y = pos2
        bracket_recursion(x, y, size * 0.5, depth - 1)


#rect(200, 100)
#rect_recursive(20, 40, 50, line_width=1)
bracket_recursion(-250, 0, 150, 5)


my_screen.exitonclick()


