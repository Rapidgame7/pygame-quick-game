import collision_bullshit as Fuck
from ent import Ent

class Gamestate:
    ents = []
    scrsq = 768
    hbound = 32
    vbound = 32

    score = 0

    def spawnPlayer(self):
        ply = Ent("player")
        ply.x = self.scrsq/2
        ply.y = self.scrsq/2
        self.ents.insert(0, ply)

    def spawnCoin(self):
        coin = Ent("coin")
        coin.x = self.scrsq/2
        coin.y = (self.scrsq/2) + 128
        self.ents.append(coin)
    
    def restartGame(self):
        self.ents.clear()
        self.spawnPlayer()
        self.spawnCoin()
        self.score = 0

    def castCollisionChecks(self):
        ents = self.ents
        for i1 in range( len(ents) ):
            e1 = ents[i1]
            for i2 in range( i1+1, len(ents) ):
                e2 = ents[i2]
                if Fuck.checkEntCollide(e1, e2):
                    #print("TOUCHY")
                    e1.castCollDaemon(self, e2)
                    e2.castCollDaemon(self, e1)
                    #bruh

    def castDaemons(self):
        for ent in self.ents:
            #ent.daemon(ent, self)
            ent.castDaemon(self)
