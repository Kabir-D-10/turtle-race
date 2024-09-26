import pgzrun
from random import randint

WIDTH =  500
HEIGHT = 500
TITLE = "Alien"

message = ""

alien = Actor('alien')

def draw():
    screen.clear()
    screen.fill((150,0,0))
    alien.draw()
    screen.draw.text(message, center = (400, 10), fontsize= 30)

def place_alien():
    alien.x = randint(50, WIDTH-50)
    alien.y = randint(50, WIDTH-50)
def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "Good Shot"
        place_alien()
    else:
        message = "You missed"


place_alien()
pgzrun.go()