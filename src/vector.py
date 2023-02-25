class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def max_component_length(self):
    return max(abs(self.x), abs(self.y))
    
  def add(self, other):
    return Vector(self.x+other.x, self.y+other.y)
  def subtract(self, other):
    return Vector(self.x-other.x, self.y-other.y)
  def multiply(self, scalar):
    return Vector(self.x*scalar,self.y*scalar)
  def divide(self, scalar):
    return Vector(self.x/scalar, self.y/scalar)
  def to_tuple(self):
    return (self.x, self.y)


