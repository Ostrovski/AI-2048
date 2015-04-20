from collections import namedtuple


Cell = namedtuple('Cell', ('x', 'y', 'v'))


class Field:
    def __init__(self, cells):
        self._dim_x = len(cells[0])
        self._dim_y = len(cells)
        self._cells = []
        for y, row in enumerate(cells):
            for x, c in enumerate(row):
                self._cells.append(Cell(x, y, c))

    def __iter__(self):
        self._iter_offset = 0
        return self

    def __next__(self):
        while self._iter_offset < len(self._cells):
            self._iter_offset += 1
            return self._cells[len(self._cells) - self._iter_offset - 1]
        raise StopIteration()

    def column(self, n):
        return [c for c in self._cells if c.x == n]

    def move_left(self):
        pass

    def row(self, n):
        return [c for c in self._cells if c.y == n]

State = namedtuple('State', ('score', 'field'))


class Problem:
    def __init__(self, dim_x=4, dim_y=4):
        self.dim_x = dim_x
        self.dim_y = dim_y

    @property
    def state(self):
        return State(300, Field(((2, 4, 8, 16),
                                 (32, 64, 128, 256),
                                 (512, 1024, 2048, 0),
                                 (0, 0, 0, 0))))