from territory import Territory

class Map:
    def __init__(self):
        self.territories = []

        gibson = Territory("gibson")
        ohio = Territory("ohio")
        sol = Territory("sol")
        fish = Territory("fish")

        gibson.create_link(sol)
        gibson.create_link(ohio)
        gibson.create_link(fish)
        fish.create_link(sol)

        return
    


