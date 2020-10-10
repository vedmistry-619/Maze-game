from turtle import *
from random import random
from freegames import line

def draw():
    "Make Maze"
    color('black')
    width(5)

    for a in range(-200,200,40):
        for b in range(-200,200,40):
            if random()>0.5:
                line(a,b,a+40,b+40)
            else:
                line(a,b+40,a+40,b)
    update()

def move():
    "Draw line and dot"
    if abs(x)>198 or abs(y)>198:
        up()
    else:
        down()

    width(2)
    color('blue')
    goto(x,y)
    dot(4)

setup(420,420,370,0)
hideturtle()
tracer(False)
draw()
onscreenclick(move)
done()
