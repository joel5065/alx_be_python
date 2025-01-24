class Shape:
  def area(self):
    raise NotImplementedError

class Rectangle(Shape):
  def area(length, width):
    return length * width

class Circle(Shape):
  def area(radius):
    return radius * math.pi
