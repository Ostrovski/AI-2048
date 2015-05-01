import unittest

from problem import Field


class FieldTestCase(unittest.TestCase):
    def test_move_left(self):
        for f in self._fixtures_left:
            field = Field(f['before'])
            field.move_left()
            self.assertEquals(f['after'], field.cells, ('move_left', f))

    def test_move_right(self):
        for f in self._fixtures_right:
            field = Field(f['before'])
            field.move_right()
            self.assertEquals(f['after'], field.cells, ('move_right', f))

    def t1est_move_up(self):
        for f in self._fixtures_up:
            field = Field(f['before'])
            field.move_up()
            self.assertEquals(f['after'], field.cells, ('move_up', f))

    def test_move_down(self):
        for f in self._fixtures_down:
            field = Field(f['before'])
            field.move_down()
            self.assertEquals(f['after'], field.cells, ('move_down', f))

    def _fixtures(self, direction):
        left = (
            {'before': ((0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},

            {'before': ((2, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((2, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},

            {'before': ((0, 2, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((2, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},

            {'before': ((0, 0, 0, 2), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((2, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},

            {'before': ((2, 0, 0, 2), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((4, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},

            {'before': ((2, 2, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((4, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},

            {'before': ((2, 2, 2, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((4, 2, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},

            {'before': ((8, 8, 8, 8), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((16, 16, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},

            {'before': ((8, 8, 4, 4), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((16, 8, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},

            {'before': ((8, 4, 4, 2), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((8, 8, 2, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},

            {'before': ((8, 0, 8, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((16, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},

            {'before': ((4, 0, 2, 2), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((4, 4, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},
        )

        right = (
            {'before': ((0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},

            {'before': ((0, 0, 0, 2), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((0, 0, 0, 2), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},

            {'before': ((0, 0, 2, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((0, 0, 0, 2), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},

            {'before': ((2, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((0, 0, 0, 2), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},

            {'before': ((2, 0, 0, 2), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((0, 0, 0, 4), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},

            {'before': ((2, 2, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((0, 0, 0, 4), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},

            {'before': ((2, 2, 2, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((0, 0, 2, 4), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},

            {'before': ((8, 8, 8, 8), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((0, 0, 16, 16), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},

            {'before': ((8, 8, 4, 4), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((0, 0, 16, 8), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},

            {'before': ((8, 4, 4, 2), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((0, 8, 8, 2), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},

            {'before': ((8, 0, 8, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((0, 0, 0, 16), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},

            {'before': ((4, 0, 2, 2), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
             'after': ((0, 0, 4, 4), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))},
        )

        return {'l': lambda: left,
                'r': lambda: right,
                'u': lambda: self._rotate(left),
                'd': lambda: self._rotate(right)}[direction]()

    @property
    def _fixtures_down(self):
        return self._fixtures('d')

    @property
    def _fixtures_left(self):
        return self._fixtures('l')

    @property
    def _fixtures_right(self):
        return self._fixtures('r')

    @property
    def _fixtures_up(self):
        return self._fixtures('u')

    def _rotate(self, fixtures):
        result = []
        for f in fixtures:
            before = [[0]*4 for _ in range(4)]
            after = [[0]*4 for _ in range(4)]
            for y in range(4):
                for x in range(4):
                    after[x][y] = f['after'][3-y][x]
                    before[x][y] = f['before'][3-y][x]
            result.append({'after': tuple(tuple(a) for a in after),
                           'before': tuple(tuple(b) for b in before)})
            print(f, {'after': tuple(tuple(a) for a in after),
                      'before': tuple(tuple(b) for b in before)})
        return tuple(result)
"""
     1  2  3  4
     5  6  7  8
     9 10 11 12
    13 14 15 16

    13  9  5  1
    14 10  6  2
    15 11  7  3
    16 12  8  4

    ( 0, 0)->( 3, 0)
    ( 1, 0)->( 3, 1)
    ( 2, 0)->( 3, 2)
    ( 3, 0)->( 3, 3)

    ( 0, 1)->( 2, 0)
    ( 1, 1)->( 2, 1)
    ( 2, 1)->( 2, 2)
    ( 3, 1)->( 2, 3)
"""