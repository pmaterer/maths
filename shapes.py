from __future__ import annotations
from mpl_toolkits.mplot3d.axes3d import Axes3D
from vector import Vector, distance
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
import colors

Origin = Vector(0, 0)

class Points(object):
    def __init__(self, *vertices: list[Vector], color: str = colors.blue, depthshade: bool = False) -> None:
        self.vertices = list(vertices)
        self.color = color
        self.depthshade = depthshade

    def draw(self, ax: plt.Axes) -> None:
        xv = [v.x for v in self.vertices]
        yv = [v.y for v in self.vertices]
        if isinstance(ax, Axes3D):
            ax.scatter(xv, yv, color=self.color, depthshade=self.depthshade)
        else:
            ax.scatter(xv, yv, color=self.color)

    def get_vertices(self) -> list[Vector]:
        return self.vertices


class FancyArrow3D(FancyArrow3D):
    def __init__(self, xs, ys, zs, *args, **kwargs) -> None:
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs
    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

class Arrow(object):
    def __init__(
        self, tip: Vector, tail: Vector = Origin, color: str = colors.blue
    ) -> None:
        self.tip = tip
        self.tail = tail
        self.color = color

    def draw(self, ax: plt.Axes) -> None:
        length = (ax.get_xlim()[1] - ax.get_xlim()[0]) / 40
        ax.arrow(
                self.tail.x,
                self.tail.y,
                self.tip.x,
                self.tip.y,
                length_includes_head=True,
                head_length=length,
                head_width=length / 2,
                fc=self.color,
                ec=self.color,
            )

    def get_vertices(self) -> list[Vector]:
        return [self.tip, self.tail]


class Polygon(object):
    def __init__(
        self,
        *vertices: list[Vector],
        color: str = colors.blue,
        fill: str = None,
        alpha: float = 0.4
    ) -> None:
        self.vertices = list(vertices)
        self.color = color
        self.fill = fill
        self.alpha = alpha

    def draw(self, ax: plt.Axes) -> None:
        for i in range(0, len(self.vertices)):
            x1, y1 = self.vertices[i].x, self.vertices[i].y
            next = (i + 1) % len(self.vertices)
            x2, y2 = self.vertices[next].x, self.vertices[next].y
            ax.plot([x1, x2], [y1, y2], color=self.color)
        if self.fill:
            xv = [v.x for v in self.vertices]
            yv = [v.y for v in self.vertices]
            ax.fill(xv, yv, color=self.color)

    def translate(self, translation: float) -> Polygon:
        translated_vertices = []
        for v in self.vertices:
            translated_vertices.append(v + translation)
        return self.__class__(*translated_vertices)

    def get_vertices(self) -> list[Vector]:
        return self.vertices

    def perimeter(self) -> float:
        distances = []
        for i in range(0, len(self.vertices)):
            distances.append(
                distance(self.vertices[i], self.vertices[(i + 1) % len(self.vertices)])
            )
        return sum(distances)


class Segment(object):
    def __init__(
        self, end: Vector, start: Vector = Origin, color: str = colors.blue
    ) -> None:
        self.start = start
        self.end = end
        self.color = color

    def draw(self, ax: plt.Axes) -> None:
        x1, y1 = self.start.x, self.start.y
        x2, y2 = self.end.x, self.end.y
        ax.plot([x1, x2], [y1, y2], color=self.color)

    def get_vertices(self) -> list[Vector]:
        return [self.start, self.end]
