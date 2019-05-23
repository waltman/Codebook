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

    def show_grid(self):
        for row in range(self._rows):
            for col in range(self._cols):
                print(self._grid[row][col].bitfield(), end=' ')
            print('')

    def _padded_bitfield(self):
        # Returns a 0-padded bitfield to make the logic simpler in_corner() 
        bitfield = []
        line = [0] * (self._cols + 2)
        bitfield.append(line)

        for row in range(self._rows):
            line = [0] + [self._grid[row][col].bitfield() for col in range(self._cols)] + [0]
            bitfield.append(line)

        line = [0] * (self._cols + 2)
        bitfield.append(line)

        return bitfield

    def _corner(self, bitfield, row, col):
        # This is the tricky part. Which corner piece should we use?
        corner = {
            (False, False, False, False): ' ',
            (False, False, False, True ): '╷',
            (False, False, True , False): '╶', 
            (False, False, True , True ): '┌',
            (False, True , False, False): '╴',
            (False, True , False, True ): '┐',
            (False, True , True , False): '─',
            (False, True , True , True ): '┬',
            (True , False, False, False): '╵',
            (True , False, False, True ): '│',
            (True , False, True , False): '└',
            (True , False, True , True ): '├',
            (True , True , False, False): '┘',
            (True , True , False, True ): '┤',
            (True , True , True , False): '┴',
            (True , True , True , True ): '┼',
        }

        nw = bitfield[row+1][col+1]
        ne = bitfield[row+1][col+2]
        sw = bitfield[row+2][col+1]
        se = bitfield[row+2][col+2]

        top = nw & 2 == 0
        left = nw & 4 == 0
        right = False if ne == 0 else ne & 4 == 0
        bottom = False if sw == 0 else sw & 2 == 0

        return corner[(top, left, right, bottom)]
    
    def contents_of(self, cell):
        return "   "

    def __str__(self):
        # draw top row
        out = "┌"
        for col in range(self._cols-1):
            cell = self._grid[0][col]
            if cell.is_linked(cell.east):
                out += "────"
            else:
                out += "───┬"
        out += "───┐\n"

        bitfield = self._padded_bitfield()
        for row in range(self._rows):
            cell = self._grid[row][0]
            top = "│"
            last_row = cell.south is None
            if last_row:
                bottom = "└"
            else:
                bottom = "│" if cell.is_linked(cell.south) else "├"

            for col in range(self._cols):
                cell = self._grid[row][col]
                body = self.contents_of(cell)
                east = " " if cell.is_linked(cell.east) else "│"
                top += body + east

                south = " " * 3 if cell.is_linked(cell.south) else "───"
                corner = self._corner(bitfield, row, col)
                bottom += south + corner

            out += top + "\n"
            out += bottom + "\n"

        return out
