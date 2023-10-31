from turtle import Turtle

BULLETCOLOUR = "#7CFC00"

class Bullet(Turtle):
    def __init__(self, pos_x):
        super().__init__()
        self.bulletcolour = BULLETCOLOUR
        self.pu()
        self.shape("square")
        self.color(self.bulletcolour)
        self.goto(pos_x, -250)
        self.shapesize(stretch_wid=1.5,stretch_len=0.3)
    def move(self):
        self.goto(self.xcor(),self.ycor()+10)
    def die(self):
        self.goto(-999,-999)
        self.ht()