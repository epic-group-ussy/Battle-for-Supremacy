

class Territory:
  def __init__(self, name):
    self.name = name
    self.team_id = -1
    self.troop_count = 0
    self.neighbors = []

  def __str__(self):
    return f"{self.name}: Team:{self.team_id}, Count{self.troop_count}"
  
  def create_link(self, t):
    if not t in self.neighbors:
      self.neighbors.append(t)
    if not self in t.neighbors:
      t.neighbors.append(self)