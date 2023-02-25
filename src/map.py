from territory import Territory
from vector import Vector

class Map:
    def __init__(self):
        self.territories = {}

        self.create_territory(Territory("gibson", Vector(0, 0)))
        self.create_territory(Territory("ohio", Vector(0, 1)))
        self.create_territory(Territory("sol", Vector(1, 0)))
        self.create_territory(Territory("fish", Vector(-1, 0)))

        return
    def create_territory(self, territory):
        self.territories[territory.name] = territory

        for other_territory_name in self.territories:
            other_territory = self.territories[other_territory_name]
            if(     territory.should_connect(other_territory)  ):
                territory.add_neighbor(other_territory)
        





