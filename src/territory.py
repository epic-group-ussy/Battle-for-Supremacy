

class Territory:
  def __init__(self, name, position):
    self.name = name
    self.position = position
    self.team_id = -1
    self.troop_count = 0

  def __str__(self):
    return f"{self.name}: Team:{self.team_id}, Count{self.troop_count}"