# pylint: disable=W0613
# w0613 coresponde a "unused argument"
import random
import pygame
import collision_bullshit as Fuck
import math
import numopers as ops
import sfx as sfx

_bbGrace = 60*1.5

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

def plyColl(ent, gs, oent):
    if ent.kind == "player":
        if oent.kind == "coin":
            sfx.playSfx("coin")
            gs.score += 1
            oent.x = random.randint(0+32, 768-32-16)
            oent.y = random.randint(0+32, 768-32-16)

            bb = gs.spawnEnt("badball")
            bb.x = random.randint(0+32, 768-32-16)
            bb.y = random.randint(0+32, 768-32-16)

            rnd = random.random()
            poss = (rnd*gs.score)/2
            print(poss)
            force = max(2, min(12, (rnd*gs.score)/2))
            ohmy = not (gs.score % 5 == 0)
            mdir = 0
            if ohmy:
                mdir = random.choice([0,90,180,270])
            else:
                mdir = random.randint(0,360)
                bb.sprite = "yelball"
            bb.momx = math.sin( math.radians(mdir) )*force
            bb.momy = math.cos( math.radians(mdir) )*force
            #bb.momy = 8

        if oent.kind == "badball" and oent.lifetime > _bbGrace:
            ent.valid = False
    if not ent.valid: sfx.stopSong()

def bbDaemon(ent, gs):
    if int(ent.lifetime/4)%2 == 0 and ent.lifetime < _bbGrace:
        ent.dodraw = False
    else: ent.dodraw = True

# pylint: disable=W
def _noDaemon(*args): pass
# pylint: enable=W
def commonDaemon(ent, gs):
    #print("sdfasdf")
    if not ent.valid:
        return
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
        "colldaemon": _noDaemon
    },
    "player": {
        "width": 16,
        "height": 16,
        "gravity": 0,
        "sprite": "ball",
        "daemon": _plyDaemon,
        "colldaemon": plyColl
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
        "sprite": "vbuck",
        "daemon": _noDaemon
    },
    "badball": {
        "width": 16,
        "height": 16,
        "sprite": "redball",
        "daemon": bbDaemon
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
