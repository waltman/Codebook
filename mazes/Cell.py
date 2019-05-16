class Cell:
    def __init__(self, row, col):
        self._row = row
        self._col = col
        self._links = set()
        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def link(self, cell, bidi=True):
        self._links.add(cell)
        if bidi:
            cell.link(self, False)

    def unlink(self, cell, bidi=True):
        self._links.remove(cell)
        if bidi:
            cell.unlink(self, False)

    def links(self):
        return list(self._links)

    def is_linked(self, cell):
        return cell in self._links

    def neighbors(self):
        return [x for x in (self.north, self.south, self.east, self.west) if x]

    def __repr__(self):
        return f'row={self._row}, col={self._col}'

    def __str__(self):
        return f'({self._row},{self._col})'

    def bitfield(self):
        bf = 0
        if self.is_linked(self.north):
            bf += 1
        if self.is_linked(self.east):
            bf += 2
        if self.is_linked(self.south):
            bf += 4
        if self.is_linked(self.west):
            bf += 8

        return bf
