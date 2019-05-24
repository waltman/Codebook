from random import choice

class Hunt_And_Kill:
    def __init__(self, grid):
        self._grid = grid
        self._create_maze()

    def _create_maze(self):
        current = self._grid.random_cell()

        while current:
            unvisited = [n for n in current.neighbors() if not n.links()]

            if unvisited:
                neighbor = choice(unvisited)
                current.link(neighbor)
                current = neighbor
            else:
                current = None

                for cell in self._grid.each_cell():
                    visited = [n for n in cell.neighbors() if n.links()]
                    if not cell.links() and visited:
                        current = cell
                        neighbor = choice(visited)
                        current.link(neighbor)
                        break
