from turtle import Turtle
from itertools import repeat

HEIGHT = .5
WIDTH = 2

class Block():
    def __init__(self):
        super().__init__()
        self.wall_blocks = {}
        self.create_wall()
        #self.block_positions = []
        #self.setheading(UP)
        #self.goto(position)
        #self.color(color)
        #self.speed("fastest")

    def block_model(self,position, color):
        turtle = Turtle("square")
        #turtle.hideturtle()
        turtle.speed("fastest")
        #turtle.shape()
        turtle.penup()
        turtle.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH, outline=0)
        turtle.goto(position)
        turtle.color(color)
        self.wall_blocks[position] = turtle
        #self.block_positions.append(position)

    def create_wall(self):
        block_colors = ()
        for color in ["red", "orange", "green", "yellow"]:
            row = tuple(repeat(color, 22))
            block_colors = block_colors + row
        color_counter = 0
        for y in range(250, 140, -15):
            for x in range(-225, 250, 45):
                self.block_model((x,y), block_colors[color_counter])
                color_counter += 1

