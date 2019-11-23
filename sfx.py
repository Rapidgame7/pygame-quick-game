# pylint: disable=W0603
import pygame
_latch = False

song = "song.ogg"

filenames = {
    #"default": "_.png",
    "coin": "coin.wav"
}
sfxs = {}

def hereWeGo():
    # call on main
    global _latch
    global song
    if not _latch:
        _latch = True
        for sstr in filenames:
            sfxs[sstr] = pygame.mixer.Sound( "res/" + filenames[sstr] )
        song = pygame.mixer.music.load("res/"+song)

def playSfx(name):
    global _latch
    if _latch == True:
        if name in sfxs:
            #return sfxs[name]
            sfxs[name].play()
    else: raise Exception("great job, you forgot the LATCH")

def playSong():
    pygame.mixer.music.play()

def stopSong():
    pygame.mixer.music.stop()
    pygame.mixer.music.rewind()