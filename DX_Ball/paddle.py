from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("cyan")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.goto(x=0, y=-280)

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(x=new_x, y=-280)

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(x=new_x, y=-280)

