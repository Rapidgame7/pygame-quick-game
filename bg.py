import images
#import pygame
import math
import random
import numopers as ops

_long = 13

class BackgroundAnim:
    x,y = 0,0
    scrollspd = 0.5
    scrollang = random.randint(0,359)
    scrollx = math.sin( math.radians(scrollang) )*scrollspd
    scrolly = math.cos( math.radians(scrollang) )*scrollspd
    ang = 0

    tile = None

    def __init__(self):
        self.tile = images.get("bggrid")
    
    def recalculateScroll(self):
        self.scrollx = math.sin( math.radians(self.scrollang) )*self.scrollspd
        self.scrolly = math.cos( math.radians(self.scrollang) )*self.scrollspd
        #print("ok")

    def daemon(self, surface):
        self.x = ops.wrap(self.x + self.scrollx, 0, 64)
        self.y = ops.wrap(self.y + self.scrolly, 0, 64)

        self.scrollang += 0.2
        self.recalculateScroll()
        #if self.x > 64: self.x -= 64
        #if self.y > 64: self.y -= 64
        for yt in range(0,_long):
            for xt in range(0,_long):
                surface.blit(self.tile, [xt*64 - self.x, yt*64 - self.y])
        #t = pygame.time.get_ticks()/10
        #rad = math.cos( math.radians(t) )*16
        #surface.blit(pygame.transform.rotate(surface, rad), [0,0])
        #surface.scroll(-64, -64)
        #surface.scroll(int(self.x), int(self.y))