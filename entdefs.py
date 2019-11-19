# pylint: disable=W0613
# w0613 coresponde a "unused argument"
#import math
import pygame
#import collision_bullshit as Fuck
import numopers as ops

def _moveBounce(ent, gs, momx, momy):
    if ent.x + ent.width + momx > gs.scrsq - gs.hbound:
        ent.momx = -ent.momx
        ent.x = gs.scrsq - gs.hbound - ent.width
    if ent.x + momx < gs.hbound:
        ent.momx = -ent.momx
        ent.x = gs.hbound
    if ent.y + ent.width + momy > gs.scrsq - gs.vbound:
        ent.momy = -ent.momy
        ent.y = gs.scrsq - gs.vbound - ent.width
    if ent.y + momy < gs.vbound:
        ent.momy = -ent.momy
        ent.y = gs.vbound

def _plyDaemon(ent, gs):
    keys = pygame.key.get_pressed()
    #print("HI MOM")
    maxspd = 8
    spdinc = 2
    #ent.momx,ent.momy = 0,0
    
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
    
    if not anyhkey: ent.momx = ops.slideToZero(ent.momx, spdinc/2)
    if not anyvkey: ent.momy = ops.slideToZero(ent.momy, spdinc/2)
    
    ent.momx = ops.clamp(ent.momx, -maxspd, maxspd)
    ent.momy = ops.clamp(ent.momy, -maxspd, maxspd)

    #print(ent.momx)

# pylint: disable=W
def _noDaemon(*args): pass
def _noCollDaemon(*args): pass
# pylint: enable=W
def commonDaemon(ent, gs):
    #print("sdfasdf")
    if not ent.valid: return
    #ent.momy += ent.gravity

    #if _moveAsFarAsPossibleSolid(ent, gs, ent.momx, 0): ent.momx = 0
    #if _moveAsFarAsPossibleSolid(ent, gs, 0, ent.momy): ent.momy = 0
    ent.x += ent.momx
    ent.y += ent.momy
    _moveBounce(ent, gs, ent.momx, ent.momy)
    #_moveBounce(ent, gs, 0, ent.momy)

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
    },
    "bad_ortho": {
        "width": 16,
        "height": 16,
        "sprite": "ball",
        "daemon": _noDaemon
    },
    "coin": {
        "width": 16,
        "height": 16,
        "sprite": "ball",
        "daemon": _noDaemon
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
