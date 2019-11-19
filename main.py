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


normfont = pygame.font.Font( pygame.font.get_default_font(), 50 )


pygame.display.set_caption("fork knife 2")


target_delay = int(1000 / 60)

bggrid = bg.BackgroundAnim()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    # predraw time
    msurf.fill(blackbg)
    
    gridsurf = pygame.Surface([768,768])
    gridsurf.blit( normfont.render("fortnite 2 pre release", True, (255,255,255)) , [0,0])
    bggrid.daemon(gridsurf)
    gridsurf.set_alpha(128)
    msurf.blit(gridsurf, [0,0])

    # game time


    # draw time

    
    pygame.display.flip()

    pygame.time.delay( target_delay )
    
