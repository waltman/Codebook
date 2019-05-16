from random import randint, choice

class Sidewinder:
    def __init__(self, grid):
        self._grid = grid
        self._create_maze()

    def _create_maze(self):
        for row in self._grid.each_row():
            run = []
            for cell in row:
                run.append(cell)
                
                at_east_bdry = cell.east is None
                at_north_bdry = cell.north is None

                should_close_out = at_east_bdry or (not at_north_bdry and randint(0, 1) == 0)

                if should_close_out:
                    member = choice(run)
                    if member.north:
                        member.link(member.north)
                    run.clear()
                else:
                    cell.link(cell.east)
