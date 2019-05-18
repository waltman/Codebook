#!/usr/bin/env python3
from sys import argv

from Grid import Grid
from Binary_Tree import Binary_Tree

rows = int(argv[1])
cols = int(argv[2])

grid = Grid(rows, cols)
maze = Binary_Tree(grid)
# grid.show_grid()
print(grid)
