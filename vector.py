from __future__ import annotations
import math
from typing import List

class Vector(object):
    def __init__(self, x: float, y: float, z: float = 0) -> None:
        self.x, self.y, self.z = x, y, z

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, v: Vector) -> Vector:
        if isinstance(v, Vector):
            x, y = self.x + v.x, self.y + v.y
        elif isinstance(v, (int, float)):
            x, y = self.x + v, self.y + v
        else:
            raise ValueError(f"cannot add '{type(v)}' and 'Vector' objects")
        return self.__class__(x, y)

    def __radd__(self, v: Vector) -> Vector:
        return self.__add__(v)

    def __sub__(self, v: Vector) -> Vector:
        if isinstance(v, Vector):
            x, y = self.x - v.x, self.y - v.y
        elif isinstance(v, (int, float)):
            x, y = self.x - v, self.y - v
        else:
            raise ValueError(f"cannot subtract '{type(v)}' and 'Vector' objects")
        return self.__class__(x, y)

    def __rsub__(self, v: Vector) -> Vector:
        return self.__sub__(v)

    def __mul__(self, v: Vector) -> Vector:
        if isinstance(v, Vector):
            return self.inner(v)
        elif isinstance(v, (int, float)):
            x = self.x * v
            y = self.y * v
            return self.__class__(x, y)
        else:
            raise ValueError(f"cannot multiply '{type(v)}' and 'Vector' objects")

    def __rmul__(self, v: Vector) -> Vector:
        return self.__mul__(v)

    def inner(self, v: Vector) -> Vector:
        """Returns the dot product (inner product) of self and another vector"""
        if not isinstance(v, Vector):
            raise ValueError("dot product requires another vector")
        return (self.x * v.x) + (self.y * v.y)

    def length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def magnitude(self) -> float:
        return self.length()

    def negate(self) -> Vector:
        negated = self * -1
        return self.__class__(negated.x, negated.y)

    def normalize(self) -> Vector:
        length = self.length()
        if length > 0:
            inverseLength = 1 / length
            x = self.x * inverseLength
            y = self.y * inverseLength
            return self.__class__(x, y)
        return self

    def to_polar(self) -> PolarVector:
        angle = math.atan2(self.y, self.x)
        return PolarVector(self.length(), angle)


def distance(v1: Vector, v2: Vector) -> float:
    return (v1 - v2).length()


def rotate(angle: float, vectors: List[Vector]) -> List[Vector]:
    polars = [v.to_polar() for v in vectors]
    rotated = []
    for p in polars:
        p.angle += angle
        rotated.append(p.to_vector())
    return rotated


class PolarVector(object):
    def __init__(self, length, angle) -> None:
        self.length = length
        self.angle = angle

    def __repr__(self) -> str:
        return f"PolarVector(length={self.length}, angle={self.angle})"

    def to_vector(self) -> Vector:
        return Vector(
            self.length * math.cos(self.angle), self.length * math.sin(self.angle)
        )
