class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def min_distance(self):
    if self.x < self.y:
      return self.x
    if self.y < self.x:
      return self.y
    


