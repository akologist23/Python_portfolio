from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
       super().__init__()
       self.shape("square")
       self.shapesize(.5,.5)
       self.penup()
       self.color("white")
       #self.goto(40,50)
       self.setheading(80)
       self.move_speed = .1

    def move(self):
        self.tiltangle(-self.heading())
        self.forward(10)

    def bounce(self):
        if 90 > self.heading() >= 0:
            if self.ycor() <= -240:
                pass
            else:
                if self.xcor() >= 235:
                    self.setheading(self.heading() + 90)
                    #print(self.heading()+.1)
                    self.forward(15)
                else:
                    self.setheading(self.heading() - 90)
                    # print(self.heading()+.1)
                    self.forward(15)
        elif 180 > self.heading() >= 90:
            if self.ycor() <= -240:
                pass
            else:
                if self.xcor() <= -245:
                    self.setheading(self.heading() - 90)
                    self.forward(15)
                else:
                    self.setheading(self.heading() + 90)
                    self.forward(15)
        elif 270 > self.heading() >= 180:
            if self.ycor() < 135:
                if self.xcor() > -245:
                    self.setheading(self.heading() - 90)
                    #print(self.heading()+.6)
                    self.forward(15)
                else:
                    self.setheading(self.heading() + 90)
                    # print(self.heading()+.6)
                    self.forward(15)
            else:
                pass
        elif 360 > self.heading() >= 270:
            if self.ycor() < 135:
                if self.xcor() >= 235:
                    self.setheading(self.heading() - 90)
                    #print(self.heading()+.8)
                    self.forward(15)
                else:
                    self.setheading(self.heading() + 90)
                    # print(self.heading()+.8)
                    self.forward(15)
            else:
                pass

    def reset_position(self):
        if self.xcor() > 0 and self.ycor() > 0:
            self.setheading(230)
        elif self.xcor() > 0 and self.ycor() < 0:
            self.setheading(140)
        elif self.xcor() < 0 and self.ycor() > 0:
            self.setheading(320)
        else:
            self.setheading(60)
        self.goto(0,0)
        #self.move_speed = 0.09