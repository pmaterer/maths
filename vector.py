import math


class Vector(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, v):
        if isinstance(v, Vector):
            x, y = self.x + v.x, self.y + v.y
        elif isinstance(v, (int, float)):
            x, y = self.x + v, self.y + v
        else:
            raise ValueError(f"cannot add '{type(v)}' and 'Vector' objects")
        return self.__class__(x, y)

    def __radd__(self, v):
        return self.__add__(v)

    def __sub__(self, v):
        if isinstance(v, Vector):
            x, y = self.x - v.x, self.y - v.y
        elif isinstance(v, (int, float)):
            x, y = self.x - v, self.y - v
        else:
            raise ValueError(f"cannot subtract '{type(v)}' and 'Vector' objects")
        return self.__class__(x, y)

    def __rsub__(self, v):
        return self.__sub__(v)

    def __mul__(self, v):
        if isinstance(v, Vector):
            return self.inner(v)
        elif isinstance(v, (int, float)):
            x = self.x * v
            y = self.y * v
            return self.__class__(x, y)
        else:
            raise ValueError(f"cannot multiply '{type(v)}' and 'Vector' objects")

    def __rmul__(self, v):
        return self.__mul__(v)

    def inner(self, v):
        """Returns the dot product (inner product) of self and another vector"""
        if not isinstance(v, Vector):
            raise ValueError(f"dot product requires another vector")
        return (self.x * v.x) + (self.y * v.y)

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
