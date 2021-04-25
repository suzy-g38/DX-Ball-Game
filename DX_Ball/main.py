from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from block import Block
from scorboard import Scoreboard

screen = Screen()
screen.title("DX Ball")
screen.bgcolor("black")
screen.setup(width=840, height=600)
screen.tracer(0)

paddle = Paddle()
ball = Ball()
block = Block()
scoreboard = Scoreboard()

block.create_block()

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Collision with wall
    ball.make_move()
    if ball.xcor() > 390 or ball.xcor() < -400:
        ball.make_bounce_x()

    # Collision with paddle
    if ball.distance(paddle) < 35 or ball.ycor() > 280:
        ball.make_bounce_y()

    # Collision with each segments in a block
    for each_seg in block.segment_list:
        if each_seg.distance(ball) < 30:
            each_seg.goto(1000, 1000)
            ball.make_bounce_y()
            ball.increase_speed()
            scoreboard.increase_score()

    # If all segments in the block are gone
    if scoreboard.score == 75:
        scoreboard.winner()

    # If ball crosses the bottom line
    if ball.ycor() < -300:
        game_is_on = False
        scoreboard.reset()
        scoreboard.game_over()

screen.exitonclick()
