from math import pi, cos, sin, atan2
from vector import Vector


def radians_to_degrees(rad):
    return rad / pi * 180


def degrees_to_radians(deg):
    return deg / 180 * pi


def to_cartesian(polar_vector):
    length = polar_vector[0]
    angle = polar_vector[1]
    return Vector(length * cos(angle), length * sin(angle))


def to_polar(v):
    angle = atan2(v.y, v.x)
    return (v.length(), angle)
