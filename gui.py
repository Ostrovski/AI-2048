from collections import defaultdict

import tkinter as tk
import tkinter.ttk as ttk

from gui_utils import square, text, draw_background


class Application(tk.Frame):
    def __init__(self, master, problem, side_size=64, border_width=8):
        tk.Frame.__init__(self, master)
        self.pack()
        master.resizable(0, 0)
        master.title('AI-2048 (Q-Learning)')
        master.configure(background='black')

        self._problem = problem
        self._side_size = side_size
        self._border_width = border_width
        self._widgets = {}

        self._create_widgets()

    def _color_cell(self, value):
        return {2: '#eee4da',
                4: '#ede0c8',
                8: '#f2b179',
                16: '#f59563',
                32: '#f67c5f',
                64: '#f65e3b',
                128: '#edcf72',
                256: '#edcc61',
                512: '#edc850',
                1024: '#edc53f',
                2048: '#edc22e'}.get(value, '#cdc0b3')

    def _color_text(self, value):
        return '#776e65' if value < 8 else '#f9f6f2'

    def _create_field(self):
        width = self._problem.dim_x*self._side_size + self._border_width*(self._problem.dim_x + 1)
        height = self._problem.dim_y*self._side_size + self._border_width*(self._problem.dim_y + 1)
        field = tk.Canvas(self, width=width, height=height)
        field.pack()
        draw_background(field, width, height, '#bbada0')
        field.update()

        self._widgets['field'] = field
        self._draw_cells(field)

    def _create_widgets(self):
        self._widgets['top_panel'] = ttk.Frame(self)
        self._widgets['top_panel'].pack(fill='x')

        self._widgets['scores'] = ttk.Label(self._widgets['top_panel'], text='Score: 0')
        self._widgets['scores'].pack(side='right')

        self._create_field()

    def _draw_cells(self, field):
        cells = defaultdict(dict)
        for c in self._problem.state.field:
            offset_left = 1 + (c.y + 1)*self._border_width + c.y*self._side_size + self._side_size/2
            offset_top = 1 + (c.x + 1)*self._border_width + c.x*self._side_size + self._side_size/2
            cell = square(field, (offset_top, offset_left), self._side_size/2, self._color_cell(c.v))
            text(field, self._text_offset((offset_top, offset_left), c.v),
                 self._color_text(c.v), c.v or None,
                 font='Helvetica Neue', size=self._text_size(c.v), style='bold')
            cells[c.x][c.y] = cell

        self._widgets['cells'] = cells

    def _text_size(self, value):
        return 24 if value > 64 else 32

    def _text_offset(self, cell_pos, value):
        offset_top, offset_left = cell_pos
        extra_top = 5 if value > 512 else (10 if value > 64 else (12 if value > 8 else 20))
        extra_left = 16 if value > 64 else 10
        return offset_top - self._side_size/2 + extra_top, \
               offset_left - self._side_size/2 + extra_left
