from turtle import Turtle

FONT = ("Terminal", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.font = FONT
        self.lives = 3
        self.color("White")
        self.pu()
        self.goto(-400,380)
        self.color("#7CFC00")
        self.update()
    def add_point(self):
        self.score += 10
        self.clear()
        self.update()
    def update(self):
        self.write(arg=self.score, align="center", font=self.font)
    def collision(self):
        self.lives -= 1
        
class Scoredisplay(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.pu()
        self.ht()
        self.goto(-455,380)
        self.write(arg="Score", align="center", font=("Terminal", 20, "normal"))
        
