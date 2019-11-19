import pygame
_latch = False

filenames = {
    "default": "_.png",
    "bggrid": "bggrid.png"
}
images = {}

def hereWeGo():
    # call on main
    _latch = True
    for sstr in filenames:
        images[sstr] = pygame.image.load( "res/" + filenames[sstr] ).convert()

def get(name):
    if _latch == True:
        if name in images:
            return images[name]
        else: return images["default"]
    else: raise Exception("great job, you forgot the LATCH")

