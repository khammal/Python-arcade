import turtle 
import os

# Create a window
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) # Stops window from updating on its own, which speeds up the game.

# Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup() 
paddle_1.goto(-350, 0) # Starting coordinates 

# Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup() 
paddle_2.goto(350, 0) # Starting coordinates 

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup() 
ball.goto(0, 0) # Starting coordinates 
ball.dx = 2
ball.dy = 2

# Scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 26, "bold"))

# Starting score
score_1 = 0
score_2 = 0


# Paddle movement
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)

# Bind keyboard keys
window.listen()
window.onkeypress(paddle_1_up, "w")
window.onkeypress(paddle_1_down, "s")
window.onkeypress(paddle_2_up, "Up")
window.onkeypress(paddle_2_down, "Down")

# Main game loop
while True:
    window.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Checking the border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # Reverses direction of the ball
        os.system("afplay assets/border_bounce.wav&") # Play sound

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 # Reverses direction of the ball
        os.system("afplay assets/border_bounce.wav&") # Play sound
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        scoreboard.clear()
        scoreboard.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 26, "bold")) 
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        scoreboard.clear()
        scoreboard.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 26, "bold"))
    
    # Paddle and ball collisions
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay assets/paddle_bounce.wav&") 


    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay assets/paddle_bounce.wav&") 

    
  