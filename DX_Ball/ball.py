from turtle import Turtle
INITIAL_SPEED = 5
SPEED_INCREMENT = 10

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.goto(x=0, y=-260)
        self.x_move = 15
        self.y_move = 15
        self.speed = INITIAL_SPEED

    def make_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def make_bounce_x(self):
        self.x_move *= -1

    def make_bounce_y(self):
        self.y_move *= -1

    def increase_speed(self):
        self.speed += SPEED_INCREMENT



