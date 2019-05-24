#!/usr/bin/env python3
from sys import argv, stderr

from Distance_Grid import Distance_Grid
from Hunt_And_Kill import Hunt_And_Kill

rows = int(argv[1])
cols = int(argv[2])

grid = Distance_Grid(rows, cols)
maze = Hunt_And_Kill(grid)

start = grid[0,0]
distances = start.distances()
new_start, distance = distances.max()

new_distances = new_start.distances()
goal, distance = new_distances.max()

grid.distances = new_distances.path_to(goal)
print(grid)
