"""
Vector module
"""
import operator
import math

from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(Decimal(n) for n in coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, vec):
        return self.coordinates == vec.coordinates


    def __add__(self, vec):
        if len(self.coordinates) != len(vec.coordinates):
            raise Exception('Vectors should have the same number of coordinates!')

        new_coordinates = map(operator.add, self.coordinates, vec.coordinates)
        return Vector(new_coordinates)


    def __sub__(self, vec):
        if len(self.coordinates) != len(vec.coordinates):
            raise Exception('Vectors should have the same number of coordinates!')

        new_coordinates = map(operator.sub, self.coordinates, vec.coordinates)
        return Vector(new_coordinates)


    def __mul__(self, factor):
        if isinstance(factor, Vector):
            new_coordinates = map(operator.mul, self.coordinates, factor.coordinates)
            return Vector(new_coordinates)

        elif isinstance(factor, (int, long, float, complex, Decimal)):
            return Vector([Decimal(factor) * coord for coord in self.coordinates])

    __rmul__ = __mul__


    def length(self):
        return Decimal(math.sqrt(sum([coord * coord for coord in self.coordinates])))


    def normalize(self):
        try:
            return self * (Decimal('1.0') / self.length())
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector!')


    def dot(self, vec):
        coords = (self * vec).coordinates
        return sum(coords)


    def angle(self, vec):
        u1 = self.normalize()
        u2 = vec.normalize()
        return math.acos(u1.dot(u2))
