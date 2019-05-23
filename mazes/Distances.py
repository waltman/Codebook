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

    def cells(self):
        return keys(self._cells)
