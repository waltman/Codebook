class Distances:
    def __init__(self, root):
        self._root = root
        self._cells = {root: 0}

    def __getitem__(self, cell):
        return self._cells[cell]

    def __setitem__(self, cell, distance):
        self._cells[cell] = distance

    def __contains__(self, cell):
        return cell in self._cells

    def path_to(self, goal):
        current = goal

        breadcrumbs = Distances(self._root)
        breadcrumbs[current] = self._cells[current]

        while current != self._root:
            for neighbor in current.links():
                if self._cells[neighbor] < self._cells[current]:
                    breadcrumbs[neighbor] = self._cells[neighbor]
                    current = neighbor

        return breadcrumbs

    def max(self):
        max_dist = 0
        max_cell = self._root

        for cell, dist in self._cells.items():
            if dist > max_dist:
                max_dist = dist
                max_cell = cell

        return max_cell, max_dist
