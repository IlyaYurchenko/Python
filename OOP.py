# Class - like coockie cutter that allows you to 
# bake coockies with defined charachteristics

#Instance - individual obj class which have an unique memory adress

class Cookie():
    #__init__ - constructor, called every time when we instantiete an obj
    def __init__(self, name, shape, chips = "chocolate"):
        self.name = name
        self.shape = shape
        self.chips = chips
    
    def bake(self):
        print(f"this {self.name} in shape of {self.shape} with {self.chips} will be bake soon")

coockie = Cookie("awesome coockie", "coockie-monster")

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

from math import pi

class Shape:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def get_area(self):
        return self.side1 * self.side2

    def __str__(self):
        return f"the are of this {self.__class__.__name__} is {self.get_area()}"

#calculating the rectangle area with get_area() func
class Rectangle(Shape):
    pass

#Polymorphism method. We changed sides by equal.
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class Triangle(Rectangle):
    def __init__(self, base, height):
        super.__init__(base, height)
    
    def get_area(self):
        area = super.get_area()
        return area/2
   
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def get_radius(self):
        pi * (self.radius ** 2)

class Hexagon(Rectangle):
    def get_area(self):
        return (3 * sqrt(3) * self.side1 ** 2 / 2)

breakpoint()