from random import randint

from Cell import Cell

class Grid:
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        
        self.prepare_grid()
        self.configure_cells()

    def __getitem__(self, rc):
        row, col = rc
        if not 0 <= row <= self._rows-1:
            return None
        if not 0 <= col <= self._cols-1:
            return None
        return self._grid[row][col]

    def each_row(self):
        for row in self._grid:
            yield(row)

    def each_cell(self):
        for row in self.each_row():
            for cell in row:
                if cell:
                    yield(cell)

    def prepare_grid(self):
        self._grid = [[Cell(row, col) for col in range(self._cols)] for row in range(self._rows)]

    def configure_cells(self):
        for cell in self.each_cell():
            row, col = cell._row, cell._col

            cell.north = self[row-1, col]
            cell.south = self[row+1, col]
            cell.west  = self[row, col-1]
            cell.east  = self[row, col+1]

    def random_cell(self):
        row = randint(0, self._rows-1)
        col = randint(0, self._cols-1)
        return self[row, col]

    def __len__(self):
        return self._rows * self._cols
    
