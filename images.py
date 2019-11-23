# pylint: disable=W0603
import pygame
_latch = False

filenames = {
    "default": "_.png",
    "bggrid": "bggrid.png",

    "ball": "ball.png",
    "redball": "redball.png",
    "vbuck": "vbuck.png"
}
images = {}

def hereWeGo():
    # call on main
    global _latch
    if not _latch:
        _latch = True
        for sstr in filenames:
            images[sstr] = pygame.image.load( "res/" + filenames[sstr] ).convert_alpha()

def get(name):
    global _latch
    if _latch == True:
        if name in images:
            return images[name]
        else: return images["default"]
    else: raise Exception("great job, you forgot the LATCH")

