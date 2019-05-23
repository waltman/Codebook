#!/usr/bin/env python3
from sys import argv, stderr

from Distance_Grid import Distance_Grid
from Binary_Tree import Binary_Tree

rows = int(argv[1])
cols = int(argv[2])

grid = Distance_Grid(rows, cols)
maze = Binary_Tree(grid)

start = grid[0,0]
distances = start.distances()
grid.distances = distances
print(grid)

print('path from northwest corner to southwest corner')
grid.distances = distances.path_to(grid[rows-1, 0])
print('attempting to print grid')
print(grid)
