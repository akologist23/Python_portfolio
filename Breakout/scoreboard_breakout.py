from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-130, 260)
        self.write(self.score, align = "center", font=("Courier", 20, "normal"))

    def point(self):
        self.score += 1
        self.update_scoreboard()

class Rounds(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.rounds = 3
        self.update_rounds()

    def update_rounds(self):
        self.clear()
        self.goto(130, 260)
        self.write(self.rounds, align="center", font=("Courier", 20, "normal"))

    def reduce_rounds(self):
        self.rounds -= 1
        self.update_rounds()