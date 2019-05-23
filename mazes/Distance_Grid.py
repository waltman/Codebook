from Grid import Grid

class Distance_Grid(Grid):
    def __init__(self, rows, cols):
        self.distances = None
        super().__init__(rows, cols)
        
    def contents_of(self, cell):
        if self.distances and cell in self.distances:
            return '{:3d}'.format(self.distances[cell])
        else:
            super().contents_of(cell)

        
        
