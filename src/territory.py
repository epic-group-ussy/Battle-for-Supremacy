import random

class Territory:
  def __init__(self, name, position):
    self.position = position

    self.name = name
    self.team_id = -1
    self.continent_id = -1
    self.troop_count = 0

    self.neighbors = []

  def __str__(self):
    return f"{self.name}: Team:{self.team_id}, Count{self.troop_count}"
  
  def should_connect(self, t2):
    return self.position.substract(t2.position).min_component_length() <= 1
  
  def add_neighbor(self, other):
    if not other in self.neighbors:
      self.neighbors.append(other)
    if not self in other.neighbors:
      other.neighbors.append(self)
    
  def get_attacked(self, num_attackers):
    """returns number to subtract from attackers"""
    defender_count = min(2, self.troop_count)
    attacker_count = min(3, num_attackers)

    defender_die = []
    attacker_die = []

    for _ in range(defender_count):
      defender_die.append(random.randint(0,6))
    for _ in range(attacker_count):
      attacker_die.append(random.randint(0,6))

    defender_die.sort(reverse=True)
    attacker_die.sort(reverse=True)

    attacker_loss = 0
    defender_loss = 0

    #compare and delete
    for i in range(min(attacker_count, defender_count)):
      if(attacker_die[i] > defender_die[i]):
        defender_loss+=1
      else:
        attacker_loss+=1
    
    self.troop_count - defender_loss
    return attacker_loss