#!/usr/bin/env python3
from sys import argv, stderr

from Grid import Grid
from Sidewinder import Sidewinder

rows = int(argv[1])
cols = int(argv[2])

grid = Grid(rows, cols)
maze = Sidewinder(grid)
# grid.show_grid()
# print(grid, file=stderr)
print(grid)
