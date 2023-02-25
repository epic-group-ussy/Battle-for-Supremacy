from territory import Territory
from vector import Vector

class Map:
    def __init__(self):
        """ALL VECTORS ARE 0,0 AS A PLACEHOLDER
        PLEASE PLEASE PLEASE DONT FORGET TO CHANGE YOU FUCKING IDIOT KILL YOURSLEF"""
        self.territories = {}
        self.colors = {}


        #GLOBAL VILLAGE (BLUE)
        self.colors["Global Village"] = "0000FF"
        
        self.GTD("GV Apartments","Global Village",Vector(1,6))
        self.GTD("Salsas","Global Village",Vector(2,5))
        self.GTD("Crossroads","Global Village",Vector(2,4))
        self.GTD("S-Lot","Global Village",Vector(2,3))
        self.GTD("Midnight Oil","Global Village",Vector(3,4))

        #FAR CAMPUS (RED)
        self.colors["Far Campus"] = "FF0000"

        self.GTD("SUS","Far Campus",Vector(3,9))
        self.GTD("Red Barn", "Far Campus",Vector(2,8))
        self.GTD("Slaughter","Far Campus",Vector(3,7))
        self.GTD("Innovation","Far Campus",Vector(3,6))
        self.GTD("Golisano","Far Campus",Vector(4,7))

        #PI QUAD (YELLOW)
        self.colors["Pi Quad"] = "FFFF00"

        self.GTD("Institute","Pi Quad",Vector(4,8))
        self.GTD("Imaging Center", "Pi Quad",Vector(5,9))
        self.GTD("Magic","Pi Quad",Vector(6,9))
        self.GTD("Ganenett","Pi Quad",Vector(6,8))
        self.GTD("F-Lot","Pi Quad",Vector(7,10))

        #INFINITY QUAD (ORANGE)
        self.colors["Infinity Quad"] = "FFA500"

        self.GTD("Orange Hall","Infinity Quad",Vector(4,5))
        self.GTD("Gleason","Infinity Quad",Vector(5,7))
        self.GTD("Gosnell","Infinity Quad",Vector(5,5))
        self.GTD("Libtard Arts","Infinity Quad",Vector(6,6))

        #SAU (TEAL)
        self.colors["SAU"] = "008080"
        
        self.GTD("U-Lot", "SAU", Vector(8,2))
        
        #KODIAK QUAD (PURPLE)
        self.colors["Kodiak Quad"] = "A020F0"

        
        self.GTD("Eastman", "Gracies Gang", Vector(7,7))
        self.GTD("Fireside", "Gracies Gang", Vector(8,6))
        self.GTD("Gym & Health center", "Gracies Gang", Vector(9,6))
        self.GTD("Shed", "Gracies Gang", Vector(7,5))
        self.GTD("Brick city", "Gracies Gang", Vector(8,5))


        #GRACIE'S GANG (GREEN)

        self.colors["Gracies gang"] = "00FF00"

        self.GTD("Colby", "Gracies Gang", Vector(11,5))


        self.GTD("Resident Halls", "Gracies Gang", Vector(10,4))
        self.GTD("Gleson", "Gracies Gang", Vector(12,4))

        self.GTD("Bike Path", "Gracies Gang", Vector(9,3))
        self.GTD("Gracies", "Gracies Gang", Vector(10,3))
        self.GTD("Baker", "Gracies Gang", Vector(11,3))

        self.GTD("Firepit", "Gracies Gang", Vector(11,2))

        self.GTD("Crack Shack", "Gracies Gang", Vector(10,1))


        #COMMONS CRUSADERS (YELLOW)

        self.colors["Commons Crusaders"] = "FFDB58"

        self.GTD("NTID", "Commons Crusaders", Vector(11,10))


        self.GTD("Commons", "Commons Crusaders", Vector(10,9))
        self.GTD("Ellingson", "Commons Crusaders", Vector(11,9))
        self.GTD("L-Lot", "Commons Crusaders", Vector(12,9))

        self.GTD("Gibson", "Commons Crusaders", Vector(11,8))

        self.GTD("Fish", "Commons Crusaders", Vector(10,7))
        self.GTD("Sol", "Commons Crusaders", Vector(12,7))

        self.GTD("NRH", "Commons Crusaders", Vector(11,6))

        #extra connections
        
        
        self.territories["F-Lot"].add_neighbor(self.territories["L-Lot"])
        self.territories["L-Lot"].add_neighbor(self.territories["U-Lot"])
        self.territories["U-Lot"].add_neighbor(self.territories["S-Lot"])
        self.territories["S-Lot"].add_neighbor(self.territories["F-Lot"])

        return
    def create_territory(self, territory):
        for other_territory_name in self.territories:
            other_territory = self.territories[other_territory_name]
            
            if(     territory.should_connect(other_territory)  ):
                territory.add_neighbor(other_territory)
        
        self.territories[territory.name] = territory


    def GTD(self,name,continent_name,vecterpos):
        """Generate Territory Data"""
        self.create_territory(Territory(name,continent_name,vecterpos))






