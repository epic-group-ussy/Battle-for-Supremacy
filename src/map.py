from territory import Territory
from vector import Vector

class Map:
    def __init__(self):
        """ALL VECTORS ARE 0,0 AS A PLACEHOLDER
        PLEASE PLEASE PLEASE DONT FORGET TO CHANGE YOU FUCKING IDIOT KILL YOURSLEF"""
        self.territories = {}


        #GLOBAL VILLAGE (BLUE)
        self.GTD("GV Apartments","Global Village",Vector(1,5))
        self.GTD("Salsas","Global Village",Vector(2,6))
        self.GTD("Crossroads","Global Village",Vector(2,7))
        self.GTD("S-Lot","Global Village",Vector(2,8))
        self.GTD("Midnight Oil","Global Village",Vector(3,7))

        #FAR CAMPUS (RED)
        self.GTD("SUS","Far Campus",Vector(3,2))
        self.GTD("Red Barn", "Far Campus",Vector(2,3))
        self.GTD("Slaughter","Far Campus",Vector(3,4))
        self.GTD("Innovation","Far Campus",Vector(3,5))
        self.GTD("Golisano","Far Campus",Vector(4,4))

        #PI QUAD (YELLOW)
        self.GTD("Institute","Pi Quad",Vector(4,3))
        self.GTD("Imaging Center", "Pi Quad",Vector(5,2))
        self.GTD("Magic","Pi Quad",Vector(6,2))
        self.GTD("Ganenett","Pi Quad",Vector(6,3))
        self.GTD("F-Lot","Pi Quad",Vector(7,1))

        #INFINITY QUAD (ORANGE)

        #SAU (TEAL)

        #KODIAK QUAD (PURPLE)

        #GRACIE'S GANG (GREEN)
        self.GTD("Colby", "Gracies Gang", Vector(6,11))

        self.GTD("Resident Halls", "Gracies Gang", Vector(6,11))
        self.GTD("Gleson", "Gracies Gang", Vector(6,11))

        self.GTD("Bike Path", "Gracies Gang", Vector(6,11))
        self.GTD("Gracies", "Gracies Gang", Vector(6,11))
        self.GTD("Baker", "Gracies Gang", Vector(6,11))

        self.GTD("Firepit", "Gracies Gang", Vector(6,11))

        self.GTD("Crack Shack", "Gracies Gang", Vector(6,11))


        #COMMONS CRUSADERS (YELLOW)
        self.GTD("NTID", "Commons Crusaders", Vector(11,1))

        self.GTD("Commons", "Commons Crusaders", Vector(10,2))
        self.GTD("Ellingson", "Commons Crusaders", Vector(11,2))
        self.GTD("L-Lot", "Commons Crusaders", Vector(12,2))

        self.GTD("Gibson", "Commons Crusaders", Vector(11,3))

        self.GTD("Fish", "Commons Crusaders", Vector(10,4))
        self.GTD("Sol", "Commons Crusaders", Vector(12,4))

        self.GTD("NRH", "Commons Crusaders", Vector(11,5))

        #extra connections

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






