import math
class Shape:
    def area(self):
        raise NotImplimentedError("Subclass should impliment this method")
class Rectangle(Shape):
    def area(self, length, width):
        self.length = length
        self.width = width
        return self.length * self.width
class Circle(Shape):
    def area(self, radius):
        self.radius = radius
        return math.pi * self.radius ** 2
       
    
    
