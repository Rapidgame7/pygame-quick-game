import images
#import pygame
#import math
#import random

_long = 13

class BackgroundAnim:
    x,y = 0,0
    ang = 0

    tile = None

    def __init__(self):
        self.tile = images.get("bggrid")

    def daemon(self, surface):
        self.x += 1 #pygame.time.get_ticks()/10
        self.y += 2 #pygame.time.get_ticks()/35
        if self.x > 64: self.x -= 64
        if self.y > 64: self.y -= 64
        for yt in range(0,_long):
            for xt in range(0,_long):
                surface.blit(self.tile, [xt*64 - self.x, yt*64 - self.y])
        #t = pygame.time.get_ticks()/10
        #rad = math.cos( math.radians(t) )*16
        #surface.blit(pygame.transform.rotate(surface, rad), [0,0])
        #surface.scroll(-64, -64)
        #surface.scroll(int(self.x), int(self.y))