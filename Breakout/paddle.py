from turtle import Turtle

MOVE_DISTANCE = 20
LEFT = 180
RIGHT = 0

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(RIGHT)
        self.shapesize(stretch_wid = 1, stretch_len = 2.5, outline = 0)
        self.goto(position)
        self.color("blue")
        self.speed("fastest")

    def left(self):
        self.backward(MOVE_DISTANCE)

    def right(self):
        self.forward(MOVE_DISTANCE)