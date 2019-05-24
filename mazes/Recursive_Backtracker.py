from random import choice

class Recursive_Backtracker:
    def __init__(self, grid):
        self._grid = grid
        self._create_maze()

    def _create_maze(self):
        stack = [self._grid.random_cell()]

        while stack:
            current = stack[-1]
            neighbors = [n for n in current.neighbors() if not n.links()]

            if neighbors:
                neighbor = choice(neighbors)
                current.link(neighbor)
                stack.append(neighbor)
            else:
                stack.pop()
