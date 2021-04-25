from turtle import Turtle
ALIGNMENT = "center"
FONT = ("FFF Forward", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.updated_scoreboard()

    def updated_scoreboard(self):
        self.clear()
        self.goto(x=0, y=250)
        self.write(f"Score : {self.score}   Highest Score: {self.high_score} ", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.updated_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.updated_scoreboard()

    def winner(self):
        self.clear()
        self.goto(x=0, y=200)
        self.write("Winner", align=ALIGNMENT, font=FONT)
        self.goto(x=0,y=130)
        self.write(f"Your Score : {self.score} ", align=ALIGNMENT, font=FONT)
        self.goto(x=0,y=60)
        self.write(f"Highest Score: {self.high_score} ", align=ALIGNMENT, font=FONT)


