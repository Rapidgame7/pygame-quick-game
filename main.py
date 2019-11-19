# pylint: disable=W0611
# Shut
import pygame, sys, os
pygame.init()
scrsize = width, height = 768, 768
msurf = pygame.display.set_mode(scrsize)
blackbg = 0, 0, 0

import images as img
img.hereWeGo()

import bg
import collision_bullshit as Fuck
from gamestate import Gamestate


normfont = pygame.font.Font( pygame.font.get_default_font(), 50 )


pygame.display.set_caption("fork knife 2")



bggrid = bg.BackgroundAnim()

target_delay = int(1000 / 60)
tickerEvent = pygame.event.custom_type()
pygame.time.set_timer(tickerEvent, target_delay)

state = Gamestate()
state.spawnPlayer()

def tick():
    pass

while 1:
    castTick = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == tickerEvent: castTick = True

    if castTick:
        # predraw time (bg stuf)
        msurf.fill(blackbg)

        gridsurf = pygame.Surface([768,768])
        gridsurf.blit( normfont.render("fortnite 2 pre release", True, (255,255,255)) , [0,0])
        bggrid.daemon(gridsurf)
        gridsurf.set_alpha(128)
        msurf.blit(gridsurf, [0,0])

        # game time
        
        state.castDaemons()
        state.castCollisionChecks()




        # draw time
        for ent in state.ents:
            spr = img.get(ent.sprite)
            if spr is not None:
                #print("french")
                pos = [ent.x, ent.y]
                msurf.blit(spr, pos)

        pygame.display.flip()

        #pygame.time.delay( target_delay )
    
