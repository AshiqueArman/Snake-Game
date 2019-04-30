import turtle
import time
import random

delay = 0.1

score = 0
highScore = 0

# Window Size

width = 600
height = 600

#  Range of SnakeFood's new Random Location after it's eaten

y1 = height/2 - 30      # limit of up
y2 = 30 - height/2      # limit of down

x1 = width/2 - 30       # limit of right
x2 = 30 - width/2       # limit of left

# creating the the main game window/canvas

window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=width, height=height)
window.tracer(0)

# SnakeHead

snakeHead = turtle.Turtle()
snakeHead.speed(0)
snakeHead.shape("circle")
snakeHead.color("red")
snakeHead.penup()
snakeHead.goto(0,0)
snakeHead.direction = "stop"

# SnakeFood

snakeFood = turtle.Turtle()
snakeFood.speed(0)
snakeFood.shape("square")
snakeFood.color("green")
snakeFood.penup()
snakeFood.goto(0,210)

# This is a list for the body part of the snake except the head

bodyPart = []

# scoreBoard

scoreBoard = turtle.Turtle()
scoreBoard.speed(0)
scoreBoard.shape("square")
scoreBoard.penup()
scoreBoard.color("white")
scoreBoard.goto(0, height/2 - 40)
scoreBoard.hideturtle()
scoreBoard.write("Score: 0 High Score: 0", align="center", font=("Comic Sans", 20, "normal"))


# Functions for moving the snake in specific direction

def go_up():
    if snakeHead.direction != "down":
        snakeHead.direction = "up"


def go_down():
    if snakeHead.direction != "up":
        snakeHead.direction = "down"


def go_right():
    if snakeHead.direction != "left":
        snakeHead.direction = "right"


def go_left():
    if snakeHead.direction != "right":
        snakeHead.direction = "left"

# Input from keyboard


window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_right, "d")
window.onkeypress(go_left, "a")


# Function for moving the snake at a fixed speed


def move():
    if snakeHead.direction == "up":
        y = snakeHead.ycor()
        snakeHead.sety(y + 20)
    if snakeHead.direction == "down":
        y = snakeHead.ycor()
        snakeHead.sety(y - 20)
    if snakeHead.direction == "right":
        x = snakeHead.xcor()
        snakeHead.setx(x + 20)
    if snakeHead.direction == "left":
        x = snakeHead.xcor()
        snakeHead.setx(x - 20)


# Main Game Loops

while True:
    window.update()

    # Border Checking

    if snakeHead.xcor() > width/2-20 or snakeHead.xcor() < 20 - width/2 or snakeHead.ycor() > height/2-20 or snakeHead.ycor() < 20 - height/2:
        time.sleep(.7)
        snakeHead.goto(0, 0)
        snakeHead.direction = "stop"

        # Hiding the body after death

        for l in bodyPart:
            l.goto(width + 10000, height + 10000)   # I am placing the snake's body out of the area of the main window
        bodyPart.clear()

        # Resetting the score

        score = 0
        scoreBoard.clear()
        scoreBoard.write(f"Score: {score} High Score: {highScore}", align="center", font=("Courier", 20, "normal"))

    # After eating the food

    if snakeHead.distance(snakeFood) < 20:
        x = random.randint(x2, x1)
        y = random.randint(y2, y1)
        snakeFood.goto(x, y)

        # Building the bodyParts

        new_bodyPart = turtle.Turtle()
        new_bodyPart.speed(0)
        new_bodyPart.shape("square")
        new_bodyPart.color("white")
        new_bodyPart.penup()
        bodyPart.append(new_bodyPart)

        # Decreasing the delay as the snake becomes bigger

        delay -= 0.0015

        # Update the score

        score += 5

        # Checking and updating the high score

        if score > highScore:
            highScore = score
        scoreBoard.clear()
        scoreBoard.write(f"Score: {score} High Score: {highScore}", align="center", font=("Courier", 20, "normal"))

    # moving the body behind the head

    for index in range(len(bodyPart) - 1, 0, -1):
        x = bodyPart[index - 1].xcor()
        y = bodyPart[index - 1].ycor()
        bodyPart[index].goto(x, y)

    # Moving the head-adjacent part of the body

    if len(bodyPart) > 0:
        x = snakeHead.xcor()
        y = snakeHead.ycor()
        bodyPart[0].goto(x, y)

    move()      # Calling the move function defined earlier

    # Collision with own body

    for k in bodyPart:
        if k.distance(snakeHead) < 20:
            time.sleep(0.7)
            snakeHead.goto(0, 0)
            snakeHead.direction = "stop"

            # Hiding the body after death

            for l in bodyPart:
                l.goto(width + 10000, height + 10000)
            bodyPart.clear()

            # Resetting the score after death

            score = 0

            # Resetting the delay after death
            delay = 0.1

            # Clearing the score board after death, but high score remains

            scoreBoard.clear()
            scoreBoard.write(f"Score: {score} High Score: {highScore}", align="center", font=("Courier", 20, "normal"))
    time.sleep(delay)

window.minloop()
