import collision_bullshit as Fuck
from ent import Ent

class Gamestate:
    ents = []

    def spawnPlayer(self):
        ply = Ent("player")
        self.ents.insert(0, ply)

    def castCollisionChecks(self):
        ents = self.ents
        for i1 in range( len(ents) ):
            e1 = ents[i1]
            for i2 in range( i1, len(ents) ):
                e2 = ents[i2]
                if Fuck.checkEntCollide(e1, e2):
                    e1.castCollDaemon(e2)
                    e2.castCollDaemon(e1)
                    #bruh

    def castDaemons(self):
        for ent in self.ents:
            #ent.daemon(ent, self)
            ent.castDaemon(self)
