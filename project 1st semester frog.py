import turtle
import random

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.bgpic("froggerscreen-2.PNG")
screen.title("Frogger Game")

# Set up the turtle
frogger = turtle.Turtle()
frogger.shape("turtle")
frogger.color("green")
frogger.penup()
frogger.goto(0, -200)
frogger.shapesize(1.4)  # 40% larger than default

# Display a text
text = turtle.Turtle()
text.penup()
text.hideturtle()
text.goto(0, 0)
text.write("Turtle has reached its destination!", align="center", font=("Arial", 16, "normal"))

# Function to move the frogger left
def move_left():
    x, y = frogger.position()
    frogger.setx(x - 10)

# Function to move the frogger right
def move_right():
    x, y = frogger.position()
    frogger.setx(x + 10)

# Function to move the frogger forward
def move_forward():
    x, y = frogger.position()
    frogger.sety(y + 10)

# Function to move the frogger backward
def move_backward():
    x, y = frogger.position()
    frogger.sety(y - 10)

# Function to quit the program using the 'q' key
def quit_program():
    screen.bye()

# Keyboard bindings
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(quit_program, "q")
screen.listen()

# This is for the title screen
title = turtle.Turtle()
title.penup()
title.hideturtle()
title.goto(0, 300)
title.write("Frogger", align="center", font=("Arial", 26, "normal"))



# Function to print final coordinates
def print_final_coordinates():
    x = frogger.xcor()
    y = frogger.ycor()
    print(f"Final Coordinates: ({x}, {y})")

# Call the function to print final coordinates
print_final_coordinates()



turtle.exitonclick()
