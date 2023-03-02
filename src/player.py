#handles the player class

class player:
    def __init__(self,name,team_id):
        self.name = name
        self.team_id = team_id
        self.troop_count = 0
        self.territories = []
        self.cards = []

    def get_new_toops_amount(self):
        """returns the amount of troops the player gets at the start of the turn"""
        #does not yet impliment contenants 
        return len(self.territories)//3 + 3