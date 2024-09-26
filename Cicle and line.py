import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 500
TITLE = "Shapes"
r = (255)
g = (255)
b = (255)
colour = (r,g,b)

def draw():
    screen.fill(colour)
    screen.draw.circle((100, 100), 50, (255, 0, 255))
    screen.draw.filled_circle((200, 250), 50,(100,100,255))
    screen.draw.line((100,400),(300,400),(0,0,0))
pgzrun.go()