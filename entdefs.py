# pylint: disable=W0613
# w0613 coresponde a "unused argument"
#import math
import pygame
#import collision_bullshit as Fuck
import numopers as ops

def _moveBounce(ent, gs, x, y):
    pass

def _plyDaemon(ent, gs):
    keys = pygame.key.get_pressed()
    #print("HI MOM")
    maxspd = 4
    spdinc = 1
    ent.momx,ent.momy = 0,0
    
    anyhkey = bool(keys[pygame.K_RIGHT] or keys[pygame.K_LEFT])
    anyvkey = bool(keys[pygame.K_UP] or keys[pygame.K_DOWN])
    #anykey = bool(anyhkey or anyvkey)

    if (keys[pygame.K_RIGHT]):
        ent.momx += spdinc
    if (keys[pygame.K_LEFT]):
        ent.momx -= spdinc
    if (keys[pygame.K_UP]):
        ent.momy -= spdinc
    if (keys[pygame.K_DOWN]):
        ent.momy += spdinc
    
    if not anyhkey: ent.momx = ops.slideToZero(ent.momx, spdinc)
    if not anyvkey: ent.momy = ops.slideToZero(ent.momy, spdinc)
    
    ent.momx = ops.clamp(ent.momx, -maxspd, maxspd)
    ent.momy = ops.clamp(ent.momy, -maxspd, maxspd)

# pylint: disable=W
def _noDaemon(*args): pass
def _noCollDaemon(*args): pass
# pylint: enable=W
def commonDaemon(ent, gs):
    #print("sdfasdf")
    if not ent.valid: return
    ent.momy += ent.gravity

    #if _moveAsFarAsPossibleSolid(ent, gs, ent.momx, 0): ent.momx = 0
    #if _moveAsFarAsPossibleSolid(ent, gs, 0, ent.momy): ent.momy = 0
    #ent.x += ent.momx
    #ent.y += ent.momy
    _moveBounce(ent, gs, ent.momx, 0)
    _moveBounce(ent, gs, 0, ent.momy)

entdefs = {
    "default": {
        "width": 0,
        "height": 0,
        "gravity": 0,
        "sprite": "error",
        "solid": False,
        "daemon": _noDaemon,
        "colldaemon": _noCollDaemon
    },
    "player": {
        "width": 16,
        "height": 16,
        "gravity": 0,
        "sprite": "ball",
        "daemon": _plyDaemon
    }
}

def get(ent):
    if ent not in entdefs:
        raise Exception("ENT DOES NOT EXIST LMAO")
    return entdefs[ent]

def getprop(ent, prop):
    me = get(ent)
    if prop not in me:
        #print("well shit this prop doesn't exist, let's check with default")
        if prop in get("default"):
            return get("default")[prop]
        else:
            raise Exception("WEIRD prop DOES NOT EXIST")
    return me[prop]
