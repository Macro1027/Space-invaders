from turtle import Turtle

SHIPCOLOUR = "#7CFC00"

class Ship(Turtle):
    def __init__(self):
        self.shipcolor = SHIPCOLOUR
        super().__init__()
        self.shape("circle")
        self.pu()
        self.color(self.shipcolor)
        self.goto(0,-250)
    def left(self):
        self.goto(self.xcor()-12, self.ycor())
    def right(self):
        self.goto(self.xcor()+12, self.ycor())