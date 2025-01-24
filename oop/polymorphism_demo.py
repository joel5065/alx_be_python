import math
class Shape:
  def area(self):
    raise NotImplementedError

class Rectangle(Shape):
  def area(self, length, width):
    return self.length * self.width

class Circle(Shape):
  def area(self, radius):
    return self.radius * math.pi
