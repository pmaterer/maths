from matplotlib import lines
import matplotlib.pyplot as plt
import numpy as np
import colors
from vector import Vector
from math import ceil, floor

Origin = Vector(0, 0, 0)


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

def draw3D(*shapes, origin=True, axes=True, elev=None, azim=None):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.view_init(elev=elev, azim=azim)

    verticies = []    
    for s in shapes:
        for v in s.get_vertices():
            verticies.append(v)
    if origin:
        verticies.append(Origin)
    
    xv = [v.x for v in verticies]
    yv = [v.y for v in verticies]
    zv = [v.z for v in verticies]

    max_x, min_x = max(0, *xv), min(0, *xv)
    max_y, min_y = max(0, *yv), min(0, *yv)
    max_z, min_z = max(0, *zv), min(0, *zv)

    x_size = max_x - min_x
    y_size = max_y - min_y
    z_size = max_z - min_z

    x_padding = 0.05 * x_size if x_size else 1
    y_padding = 0.05 * y_size if y_size else 1
    z_padding = 0.05 * z_size if z_size else 1

    plot_x_range = (min(min_x - x_padding, -2), max(max_x + x_padding, 2))
    plot_y_range = (min(min_y - y_padding, -2), max(max_y + y_padding, 2))
    plot_z_range = (min(min_z - z_padding, -2), max(max_z + z_padding, 2))

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    def draw_segment(start, end, color=colors.black, linestyle='solid'):
        xs, ys, zs = [[start[i], end[i]] for i in range(0, 3)]
        ax.plot(xs, ys, zs, color=color, linestyle=linestyle)
    
    if axes:
        draw_segment((plot_x_range[0], 0, 0), (plot_x_range[1], 0, 0))
        draw_segment((0, plot_y_range[0], 0), (0, plot_y_range[1], 0))
        draw_segment((0, 0, plot_z_range[0]), (0, 0, plot_z_range[1]))

    if origin:
        ax.scatter([0], [0], [0], color=colors.black, marker='x')

    for shape in shapes:
        shape.draw(ax)

    plt.show()