# pylint: disable=W0611
# Shut
import pygame, sys, os
import images as img

pygame.init()


normfont = pygame.font.Font( pygame.font.get_default_font(), 50 )

scrsize = width, height = 1024, 768
msurf = pygame.display.set_mode(scrsize)
black = 0, 0, 0

pygame.display.set_caption("fork knife 2")


target_delay = int(1000 / 60)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    # predraw time
    msurf.fill(black)
    msurf.blit( normfont.render("fortnite 2 pre release", True, (255,255,255)) , [0,0])
    


    # game time


    # draw time

    
    pygame.display.flip()

    pygame.time.delay( target_delay )
    
