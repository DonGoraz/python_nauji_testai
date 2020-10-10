# Python program showing
# abstract base class work
from abc import ABC, abstractmethod
# Import math Library
import math

class GeometricFigure(ABC):

    # abstract method
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def square_area(self):
        pass

class Circle(GeometricFigure):

    # class variables should be for asll class objects
    __pi = math.pi
    _radius = int()

    def __init__(self, radius):
        # instance variables should be used for instances
        self.radius = radius
        # self._radius = radius

    @property
    def radius(self):
       print(self._radius, type(self._radius))
       return self._radius

    @radius.setter
    def radius(self, radius):
        if radius > 0:
            self._radius = radius
        else:
            raise Exception("Bad radius")

    # overriding abstract method
    def perimeter(self):
        return 2 * self.radius * self.__pi
    def square_area(self):
        return 2 * self.radius * self.__pi

print(Circle._radius)
circle1 = Circle(1)
circle2 = Circle(3)
print(circle1.perimeter())
print(circle2.perimeter())
Circle._radius = 10
# circle1.radius = 10
print(circle1.perimeter(), circle1.radius)
print(circle2.perimeter(),  circle2.radius)