from random import randint

class Binary_Tree:
    def __init__(self, grid):
        self._grid = grid
        self._create_maze()

    def _create_maze(self):
        for cell in self._grid.each_cell():
            neighbors = []
            if cell.north:
                neighbors.append(cell.north)
            if cell.east:
                neighbors.append(cell.east)

            if neighbors:
                idx = randint(0, len(neighbors)-1)
                neighbor = neighbors[idx]
                cell.link(neighbor)
