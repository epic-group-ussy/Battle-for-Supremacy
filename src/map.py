from territory import Territory
from vector import Vector

class Map:
    def __init__(self):
        """ALL VECTORS ARE 0,0 AS A PLACEHOLDER
        PLEASE PLEASE PLEASE DONT FORGET TO CHANGE YOU FUCKING IDIOT KILL YOURSLEF"""
        self.territories = {}


        #GLOBAL VILLAGE (BLUE)

        #FAR CAMPUS (RED)

        #PI QUAD (YELLOW)

        #INFINITY QUAD (ORANGE)

        #SAU (TEAL)

        #KODIAK QUAD (PURPLE)

        #GRACIE'S GANG (GREEN)

        #COMMONS CRUSADERS (YELLOW)
        self.GTD("NTID", "Commons Crusaders", Vector(1,11))

        self.GTD("Commons", "Commons Crusaders", Vector(2,10))
        self.GTD("Ellingson", "Commons Crusaders", Vector(2,11))
        self.GTD("L-Lot", "Commons Crusaders", Vector(2,12))

        self.GTD("Gibson", "Commons Crusaders", Vector(3,11))

        self.GTD("Fish", "Commons Crusaders", Vector(4,10))
        self.GTD("Sol", "Commons Crusaders", Vector(4,12))

        self.GTD("NRH", "Commons Crusaders", Vector(5,11))

        return
    def create_territory(self, territory):
        self.territories[territory.name] = territory

        for other_territory_name in self.territories:
            other_territory = self.territories[other_territory_name]
            if(     territory.should_connect(other_territory)  ):
                territory.add_neighbor(other_territory)


    def GTD(self,name,continent_name,vecterpos):
        """Generate Territory Data"""
        self.create_territory(Territory(name,continent_name,vecterpos))






