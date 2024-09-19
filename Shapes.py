import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 500
TITLE = "Shapes"
r=randint(0,255)
g=randint(0,255)
b=randint(0,255)
colour = (r,g,b)

def draw():
    screen.fill(colour)
    rect1 = Rect((50,50),(100,100))
    screen.draw.rect(rect1,(255,100,100))
    filled_rect1 = Rect((200,200),(100,100))
    screen.draw.filled_rect(filled_rect1,(100,100,255))

pgzrun.go()