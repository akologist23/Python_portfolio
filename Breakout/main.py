from turtle import Screen
from scoreboard_breakout import Scoreboard, Rounds
from ball import Ball
from paddle import Paddle
from block import Block
import time

#Create Game Screen
screen = Screen()
screen.setup(width=500, height=600)
screen.bgcolor("black")
screen.title("Breakout")

#Initialize Objects on Screen
screen.tracer(0)
ball = Ball()
paddle = Paddle((0,-250))
block = Block()
scoreboard = Scoreboard()
rounds = Rounds()
screen.update()

screen.listen()
screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(.05)
    screen.update()
    scoreboard.update_scoreboard()
    rounds.update_rounds()
    ball.move()

    #detect collision with right or left walls
    if ball.xcor() >= 236:
        #print("hit right side")
        #print(ball.position())
        ball.bounce()
    elif ball.xcor() <= -245:
        #print("hit left side")
        #print(ball.position())
        ball.bounce()

    # Detect collision with blocks
    if ball.ycor() >= 135:
        #print(ball.ycor())
        removal_key = None
        for key, value in block.wall_blocks.items():
            if ball.distance(key) < 20:
               #print(f"distance: {ball.distance(key)}")
                #print(f"key: {key}")
                #print(f"ball: {ball.position()}")
                value.goto(0, -500)
                block.wall_blocks.pop(key)
                scoreboard.point()
                scoreboard.update_scoreboard()
                ball.bounce()
                ball.move_speed *= 2
                break

    #Detect collision with paddle
    if ball.distance(paddle) <= 30 and ball.ycor() <= -235:
        print("made contact")
        print(ball.position())
        ball.bounce()
        #ball.move_speed *= .95

    #Detect missed contact with paddle
    if ball.ycor() <= -250:
        rounds.reduce_rounds()
        print("round over")
        print(ball.position())
        ball.reset_position()
        if rounds.rounds == 0:
            ball.move_speed = 0
            ball.goto(0,0)
            screen.update()
            game_is_on = False

    # Detect collision with top wall
    if ball.ycor() >= 290:
        print("made contact")
        print(ball.position())
        ball.bounce()
        # ball.move_speed *= .95
screen.exitonclick()