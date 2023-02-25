from territory import Territory
from vector import Vector

class Map:
    def __init__(self):
        """ALL VECTORS ARE 0,0 AS A PLACEHOLDER
        PLEASE PLEASE PLEASE DONT FORGET TO CHANGE YOU FUCKING IDIOT KILL YOURSLEF"""
        self.territories = {}
        #DORMS CONT
        self.GTD("Gibson","Dorm",Vector(0,0))
        self.GTD("Sol","Dorm", Vector(0, 0))
        self.GTD("fish","Dorm",Vector(0, 0))

        #GLOBAL VILLAGE CONT (BLUE)

        #ATTACKING CONT
        self.GTD("Ohio","Attack",Vector(0,1))

        #FAR CAMPUS (RED)

        #PI QUAD (YELLOW)

        #INFINITY QUAD (ORANGE)

        #SAU THING (TEAL)

        #KODIAK QUAD (PURPLE)

        #GRACIE'S GANG (GREEN)

        #COMMONS LOVERS (YELLOW)


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






