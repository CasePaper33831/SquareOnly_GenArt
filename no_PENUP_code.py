import turtle
import random

# Popup shenanigans
window_width = turtle.window_width()
window_height = turtle.window_height()
turtle.bgcolor("black")
turtle1 = turtle.Turtle()
turtle1.speed(0)
turtle2 = turtle.Turtle()
turtle2.speed(0)

def generate_art():
    # Generates the turtle graphics based on user input.
    num_iterations = int(input("Enter the number of iterations for the loop (no commas): "))
    num_sides = int(input("How many sides in the square? no commas: "))
    group_size = num_sides  # "sides" of square. if above 4, spiral effect starts
    current_group = 1

    #Tells Turtle about shape angles, and pen action
    turtle1.backward(91)
    turtle1.pendown()
    turtle2.backward(91)
    turtle2.pendown()

    #used for distances between squares
    random_distance = random.uniform(70, 120)

    for i in range(num_iterations):
        # Turtle1
        turtle1.forward(random_distance)
        turtle1.left(91)
        # if exiting window, force back inside.
        x, y = turtle1.position()
        if abs(x) > window_width / 2 or abs(y) > window_height / 2:
            turtle1.setposition(0, 0)
            turtle1.pendown()


        # ...and turtle 2
        turtle2.forward(random_distance)
        turtle2.right(91)
        x, y = turtle2.position()
        if abs(x) > window_width / 2 or abs(y) > window_height / 2:
            turtle2.setposition(0, 0)
            turtle2.pendown()

        #tells turtles how to behave while drawing
        if (i + 1) % group_size == 0:
            forward_distance = random.randint(30, min(window_width, window_height) // 2)
            turtle1.forward(forward_distance)
            turn_angle = random.randint(10, 90)
            turtle1.left(turn_angle)
            turtle1.pendown()
            random_color = (random.random(), random.random(), random.random())
            turtle1.pencolor(random_color)

            forward_distance = random.randint(30, min(window_width, window_height) // 2)
            turtle2.forward(forward_distance)
            turn_angle = random.randint(10, 90)
            turtle2.right(turn_angle)
            turtle2.pendown()
            random_color = (random.random(), random.random(), random.random())
            turtle2.pencolor(random_color)
            current_group += 1

# Keep the popup open after generation
generate_art()
turtle.done()
