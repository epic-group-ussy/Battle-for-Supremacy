import random

class Territory:
  def __init__(self, name, position):
    self.position = position

    self.name = name
    self.team_id = -1
    self.continent_id = -1
    self.troop_count = 0

  def __str__(self):
    return f"{self.name}: Team:{self.team_id}, Count{self.troop_count}"
  

  def attack(self, num_attackers):
    """returns number to subtract from attackers"""
    defender_count = max(2, self.troop_count)
    attacker_count = max(3, num_attackers)

    defender_die = []
    attacker_die = []

    for _ in range(defender_count):
      defender_die.append(random.randint(0,6))
    for _ in range(attacker_count):
      attacker_die.append(random.randint(0,6))

    defender_die.sort(reverse=True)
    attacker_die.sort(reverse=True)

    #compare and delete
    for i in range(min(attacker_count, defender_count)):
      