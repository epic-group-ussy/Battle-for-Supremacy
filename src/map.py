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

    def is_connected(self, t1, t2):
        return t1.position.min_component_length(t2.position) <= 1


