from collections import namedtuple


class Cell:
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.v = v

    def __str__(self):
        return "(%s, %s): %s" % (self.x, self.y, self.v)


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

    @property
    def cells(self):
        cells, row = [], []
        for idx, c in enumerate(self._cells):
            row.append(c.v)
            if self._dim_x - 1 == idx % self._dim_x:
                cells.append(tuple(row))
                row = []
        return tuple(cells)

    def move_down(self):
        self._move('d')

    def move_left(self):
        self._move('l')

    def move_right(self):
        self._move('r')

    def move_up(self):
        self._move('u')

    def _move(self, direction):
        assert direction in ('l', 'r', 'u', 'd')
        rows_count = self._dim_y if direction in ('l', 'r') else self._dim_x
        cols_count = self._dim_x if direction in ('l', 'r') else self._dim_y
        x_start = 0
        x_end = cols_count - 1
        offset = 1
        if direction in ('r', 'd'):
            x_start, x_end = x_end, x_start
            offset = -offset

        def shift(row):
            x, skip = x_start, 0
            while 0 < abs(x - x_end):
                x += offset
                ct = self._cell(x_start + skip, row, offset < 0)
                cf = self._cell(x, row, offset < 0)
                if 0 == ct.v:
                    ct.v, cf.v = cf.v, 0
                if 0 != ct.v:
                    skip += offset

        def merge(row):
            x = x_start
            while 0 < abs(x - x_end) and 0 != self._cell(x, row, offset < 0).v:
                ct = self._cell(x, row, offset < 0)
                cf = self._cell(x + offset, row, offset < 0)
                if 0 == ct.v or ct.v == cf.v:
                    ct.v, cf.v = ct.v + cf.v, 0
                    x += offset
                x += offset

        for y in range(rows_count):
            shift(y)
            merge(y)
            shift(y)

    def _cell(self, x, y, reverse=True):
        return self._cells[y*(self._dim_y if reverse else self._dim_x) + x]

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