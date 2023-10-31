from turtle import Turtle
from random import randint
class Powerup(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.shapesize(stretch_len=2,stretch_wid=2)
        self.color("Blue")
        self.goto(randint(-300,300),randint(-300,300))
    def die(self):
        self.goto(-999,-999)
        self.ht()