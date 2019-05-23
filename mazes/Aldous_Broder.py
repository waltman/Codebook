from random import choice

class Aldous_Broder:
    def __init__(self, grid):
        self._grid = grid
        self._create_maze()

    def _create_maze(self):
        cell = self._grid.random_cell()
        unvisited = len(self._grid) - 1

        while unvisited > 0:
            neighbor = choice(cell.neighbors())
            if not neighbor.links():
                cell.link(neighbor)
                unvisited -= 1

            cell = neighbor
