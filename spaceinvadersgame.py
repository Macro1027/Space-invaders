from turtle import Turtle, Screen
from spaceinvadersship import Ship
from spaceinvadersbullet import Bullet
from spaceinvadersalien import Invader
from spaceinvadersscoreboard import Scoreboard, Scoredisplay
from spaceinvaderspowerups import Powerup
from time import sleep
from random import randint
import datetime
import os

screen = Screen()
screen.setup(width=1000, height=1200)
screen.title("Space Invaders Ripoff by Marco")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

alien = os.path.expanduser("~/Desktop/Scrnshot/invader.gif")
screen.addshape(alien)
ship = Ship()
invaders = []
bullets = []
powerups = []
scoreboard = Scoreboard()
score = Scoredisplay()


current = [(str(datetime.datetime.now())[-9:])] * 3
level = 1
firespeed = 0.3

def spawn_aliens(move_speed):
    for x in range(-3500,3501,684):
        for y in range(0,2500, 492):
            invaders.append(Invader(alien, x/10, y/10, move_speed))
            
def cooldown(seconds, current_index):
    return abs(float(str(datetime.datetime.now())[-9:]) - float(current[current_index])) > seconds

def fire():
    if cooldown(firespeed, 0):
        bullets.append(Bullet(ship.xcor()))
        current[0] = (str(datetime.datetime.now())[-9:])

def powerup():
    if cooldown(5, 1):
        if randint(1,100) == 1:
            powerups.append(Powerup())
            current[1] = (str(datetime.datetime.now())[-9:])
def reset_powerup():
    global firespeed
    if cooldown(5, 2):
        firespeed = 0.3

def next_wave(move_speed):
    global level
    if len(invaders) <= 5:
        spawn_aliens(move_speed * level)
        level += 1

def lose():
    screen.textinput("You have lost.")
game_is_on = True

keys_pressed = {}
def pressed(event):
    keys_pressed[event.keysym] = True
def released(event):
    keys_pressed[event.keysym] = False
def set_key_binds():
    for key in ["Left", "Right", "space"]:
        screen.getcanvas().bind(f"<KeyPress-{key}>", pressed)
        screen.getcanvas().bind(f"<KeyRelease-{key}>", released)
        keys_pressed[key] = False
set_key_binds()


if __name__ == '__main__':
    go_down = False
    while game_is_on:
        reset_powerup()
        next_wave(2.5)
        if keys_pressed["Left"]: ship.left()
        if keys_pressed["Right"]: ship.right()
        if keys_pressed["space"]: fire()
        
        for i in bullets:
            i.move()
        for aliens in invaders:
            if aliens.ycor() < -240:
                aliens.die()
                invaders.remove(aliens)
                scoreboard.collision()
            if aliens.xcor() > 450 or aliens.xcor() < -450:
                aliens.direction *= -1
                aliens.down()
            aliens.move()
            for b in bullets:
                if aliens.distance(b) < 28.5:
                    b.die()
                    bullets.remove(b)
                    aliens.die()
                    invaders.remove(aliens)
                    scoreboard.add_point()
                if b.ycor() > 450:
                    b.die()
                    bullets.remove(b)
                for p in powerups:
                    if b.distance(p) < 20:
                        p.die()
                        powerups.remove(p)
                        current[2] = (str(datetime.datetime.now())[-9:])
                        firespeed = 0.15
            
                    
                    
        if scoreboard.lives == 0:
            screen.textinput("You have lost.", "Get better.")
            screen.bye()
        powerup()
        screen.update()
    screen.exitonclick()
