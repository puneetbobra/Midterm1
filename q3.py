# Hit the Target Game
import turtle
import math

# Named constants
SCREEN_WIDTH = 600    # Screen width
SCREEN_HEIGHT = 600   # Screen height
MAX_DISTANCE = math.ceil(math.sqrt(SCREEN_HEIGHT ** 2 + SCREEN_HEIGHT ** 2) / 2)

TARGET_CENTER_X = 100  # Target's center X
TARGET_CENTER_Y = 250  # Target's center Y
TARGET_RADIUS = 30     # raidus of the target

PROJECTILE_SPEED = 1  # Projectile's animation speed

# Setup the window
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

pen = turtle.Pen()

# Draw the target.
pen.hideturtle()
pen.speed(0)
pen.penup()
pen.goto(TARGET_CENTER_X, TARGET_CENTER_Y - TARGET_RADIUS)
pen.pendown()
pen.circle(TARGET_RADIUS)
pen.penup()

#Go to center
pen.home()
pen.showturtle()
pen.speed(PROJECTILE_SPEED)

SENTINEL = -1

# Keep looping until user hits the target circle
while True:
    angle = int(input("Enter the projectile's angle 0-360 (-1 to stop the program): "))
    distance = int(input(f'Enter the launch distance (1-{MAX_DISTANCE}) (-1 to stop the program): '))
# if user enters -1 as angle or distance then stop the program
    if angle == SENTINEL or distance == SENTINEL: 
        print('\nProgram stopped, exit the drawing window')
        break
# Set the heading.
    pen.setheading(angle)
# Launch the projectile.
    pen.pendown()
    pen.forward(distance)
    xcor = pen.xcor()
    ycor = pen.ycor()
# distance to the center of the circle can be calculated as sqrt((x1 – x2)**2 + (y1 – y2)**2)
# distance from the edge of the cirlce to the center is the radius
# hence sqrt((x1 – x2)**2 + (y1 – y2)**2) = radius OR (x1 – x2)**2 + (y1 – y2)**2 <= radius**2
    if (xcor - TARGET_CENTER_X)**2 + (ycor - TARGET_CENTER_Y)**2 <= TARGET_RADIUS**2: 
        print('Target hit')
        break
 # Go back to home for a new trial by the user
    else: pen.home()
   

turtle.done()