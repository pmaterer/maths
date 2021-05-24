import matplotlib.pyplot as plt
import numpy as np
from math import ceil, floor


def draw(*shapes, grid=(1, 1), origin=True, axes=True, width=8):
    fig, ax = plt.subplots()

    vertices = []
    for s in shapes:
        for v in s.get_vertices():
            vertices.append(v)

    xv = [v.x for v in vertices]
    yv = [v.y for v in vertices]

    max_x, min_x, max_y, min_y = max(0, *xv), min(0, *xv), max(0, *yv), min(0, *yv)

    if origin:
        ax.scatter([0], [0], color="k", marker="x")

    if grid:
        x_padding = max(ceil(0.05 * (max_x - min_x)), grid[0])
        y_padding = max(ceil(0.05 * (max_y - min_y)), grid[1])

        xlim_min = floor((min_x - x_padding) / grid[0]) * grid[0]
        xlim_max = ceil((max_x + x_padding) / grid[0]) * grid[0]
        ax.set_xlim(xlim_min, xlim_max)

        ylim_min = floor((min_y - y_padding) / grid[1]) * grid[1]
        ylim_max = ceil((max_y + y_padding) / grid[1]) * grid[1]
        ax.set_ylim(ylim_min, ylim_max)

        ax.set_xticks(np.arange(ax.get_xlim()[0], ax.get_xlim()[1], grid[0]))
        ax.set_yticks(np.arange(ax.get_ylim()[0], ax.get_ylim()[1], grid[1]))
        ax.grid(True)
        ax.set_axisbelow(True)

    if axes:
        ax.axhline(linewidth=2, color="k")
        ax.axvline(linewidth=2, color="k")

    coords_height = ax.get_ylim()[1] - ax.get_ylim()[0]
    coords_width = ax.get_xlim()[1] - ax.get_xlim()[0]
    fig.set_size_inches(width, width * coords_height / coords_width)

    for shape in shapes:
        shape.draw(ax)

    plt.show()
