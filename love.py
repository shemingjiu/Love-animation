import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Love Animation")

# Create the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(3)
pen.hideturtle()

# Draw a heart function
def draw_heart(size):
    pen.color("pink")
    pen.begin_fill()
    pen.left(140)
    pen.forward(size)
    pen.circle(-size / 2, 200)
    pen.left(120)
    pen.circle(-size / 2, 200)
    pen.forward(size)
    pen.end_fill()

# Write the "I love you Jason" text
def write_text():
    pen.penup()
    pen.goto(0, -20)
    pen.color("white")
    pen.write("I love you Jason", align="center", font=("Arial", 24, "bold"))
    pen.hideturtle()

# Function for drawing twinkling stars
def draw_star(x, y, size):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(random.randint(0, 360))
    pen.color("yellow")
    pen.pendown()
    pen.begin_fill()
    for _ in range(5):
        pen.forward(size)
        pen.right(144)
    pen.end_fill()

# Animate the heart and stars
def animate():
    pen.clear()
    
    # Draw the moving heart
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    size = 120 + 10 * random.uniform(-1, 1)
    draw_heart(size)
    
    # Draw random twinkling stars
    for _ in range(15):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        size = random.randint(5, 15)
        draw_star(x, y, size)

    # Write the text
    write_text()
    
    # Call this function again for continuous animation
    screen.ontimer(animate, 500)

# Start the animation
animate()
screen.mainloop()
