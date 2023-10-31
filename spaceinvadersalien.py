from turtle import Turtle

class Invader(Turtle):
    def __init__(self, image, start_x, start_y, move_speed):
        super().__init__()
        self.pu()
        self.goto(start_x, start_y)
        self.shape(image)
        self.direction = 1
        self.move_speed = move_speed
    def die(self):
        self.goto(-999,-999)
        self.ht()
    def move(self):
        if self.direction == 1:
            self.goto(self.xcor()+self.move_speed,self.ycor())
        if self.direction == -1:
            self.goto(self.xcor()-self.move_speed,self.ycor())
    def down(self):
        self.goto(self.xcor(),self.ycor()-49.2)
        