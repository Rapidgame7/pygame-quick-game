import entdefs as ed
#import sprites as sprites


class Ent:
    valid = True # invalid ents are removed at the end of the day
    #gravity = 0.5 No sirve aca
    kind = "unknown"
    solid = False

    width, height = 32,32

    x,y = 0,0 # Pos
    momx,momy = 0,0 # momentum across axis

    gx,gy = 0,0 # Graphic pos
    gang = 0

    lifetime = 0

    sprite = "error"

    #fuckingdie = False

    def __init__(self, kind):
        #kind has to be an entdef index i spose lol
        #me = ed.get(kind)
        self.kind = kind #bro
        self.width = ed.getprop(kind, "width")
        self.height = ed.getprop(kind, "height")
        #self.gravity = ed.getprop(kind, "gravity")
        self.sprite = ed.getprop(kind, "sprite")
        self.solid = ed.getprop(kind, "solid")
        self.daemon = ed.getprop(kind, "daemon")
        self.colldaemon = ed.getprop(kind, "colldaemon")

    def castDaemon(self, gs):
        self.lifetime += 1
        ed.commonDaemon(self, gs)
        self.daemon(self, gs)
    
    def castCollDaemon(self, gs, other):
        self.colldaemon(self, gs, other)

    def _assign(self, kind):
        #entdefs["none"]["daemon"](self)
        pass

    def setpos(self, x, y):
        self.x = x
        self.y = y

    def kill(self):
        self.valid = False

        

