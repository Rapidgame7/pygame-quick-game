#import ent

class FakeEnt:
    x,y,width,height = 0,0,0,0

    def __init__(self, ent=None):
        if ent is not None: self.copyStats(ent)

    def copyStats(self, ent):
        self.x, self.y, self.width, self.height = ent.x, ent.y, ent.width, ent.height
    
    def sumStats(self,x,y,w,h):
        self.x += x
        self.y += y
        self.width += w
        self.height += h

def _unicheck(m1, h1, m2, h2):
    # unidimensional collision check
    #print(str(m1)+" <= "+str(m2+h2)+" | "+str(m1+h1)+" > "+str(m2))
    return bool(m1 < m2+h2 and m1+h1 > m2)

def checkPointCollide(x1, y1, h1, w1, xp, yp):
    return bool(_unicheck(y1, h1, yp, 0) and _unicheck(x1, w1, xp, 0))

def checkRectCollide(x1, y1, h1, w1, x2, y2, h2, w2):
    return bool(_unicheck(y1, h1, y2, h2) and _unicheck(x1, w1, x2, w2))

def checkEntCollide(ent1, ent2):
    return checkRectCollide( ent1.x, ent1.y, ent1.height, ent1.width, ent2.x, ent2.y, ent2.height, ent2.width )
def checkEntPointCollide(ent1, px, py):
    return checkPointCollide( ent1.x, ent1.y, ent1.height, ent1.width, px, py )
def checkEntCollideMom(ent1, ent2):
    return checkRectCollide( ent1.x+ent1.momx, ent1.y+ent1.momy, ent1.height+ent1.momy, ent1.width+ent1.momx,
                             ent2.x+ent2.momx, ent2.y+ent2.momy, ent2.height+ent2.momy, ent2.width+ent2.momx )




# bro