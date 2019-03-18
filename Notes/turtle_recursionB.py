import turtle

my_turtle = turtle.Turtle()  # create a turtle object
my_screen = turtle.Screen()  # create a screen object

my_turtle.width(4)
my_turtle.speed(0)
my_turtle.shape("turtle")

my_turtle.penup()
my_turtle.goto(0, 0)  # sends it to a point without turning
my_turtle.goto(100, 100)
my_turtle.pendown()
my_turtle.goto(100, 0)

my_turtle.forward(50)
my_turtle.left(45)
my_turtle.forward(100)
my_turtle.right(45)
my_turtle.backward(100)
my_turtle.setheading(180)  # turn to a heading

# make a shape
my_turtle.fillcolor("lightblue")
my_turtle.begin_fill()  # start my shape
for i in range(12):
    my_turtle.forward(50)
    my_turtle.right(30)
my_turtle.end_fill()  # end the shape and fill it

my_turtle.penup()
my_turtle.goto(0, 0)
my_turtle.pendown()
my_turtle.pencolor("black")

distance = 10
for i in range(100):
    my_turtle.forward(distance + i)
    my_turtle.left(15)

my_screen.clear()

def recursive_rect(line_width, width, height, depth):
    if depth > 0:
        my_turtle.width(line_width)
        my_turtle.penup()
        my_turtle.goto(-width / 2, height / 2)  # top left corner
        my_turtle.setheading(0)
        my_turtle.pendown()
        for i in range(2):
            my_turtle.forward(width)
            my_turtle.right(90)
            my_turtle.forward(height)
            my_turtle.right(90)
        recursive_rect(line_width * 1.1, width * 1.1, height * 1.1, depth - 1)

recursive_rect(1, 20, 50, 40)





my_screen.exitonclick()




