def clear_field(canvas, width=None, height=None, color=None):
    canvas.delete('all')
    if width and height and color:
        draw_background(canvas, width, height, color)


def draw_background(canvas, width, height, color):
    corners = [(0, 0), (0, height), (width, height), (width, 0)]
    polygon(canvas, corners, color, fill_color=color, filled=True, smoothed=False, width=0)


def polygon(canvas, coords, outline_color, fill_color=None,
            filled=1, smoothed=1, width=1, behind=0):
    c = []
    for coord in coords:
        c.append(coord[0])
        c.append(coord[1])

    if not filled:
        fill_color = ''
    else:
        fill_color = fill_color or outline_color

    poly = canvas.create_polygon(c, outline=outline_color, fill=fill_color,
                                 smooth=smoothed, width=width)

    if behind > 0:
        canvas.tag_lower(poly, behind)

    return poly


def square(canvas, pos, r, color, filled=1, behind=0):
    x, y = pos
    coords = [(x - r, y - r), (x + r, y - r), (x + r, y + r), (x - r, y + r)]
    return polygon(canvas, coords, color, color, filled, 0, behind)


def text(canvas, pos, color, contents, font='Helvetica', size=12, style='normal', anchor='nw'):
    x, y = pos
    font = (font, str(size), style)
    return canvas.create_text(x, y, fill=color, text=contents, font=font, anchor=anchor)

# def change_text(id, newText, font=None, size=12, style='normal'):
#     _canvas.itemconfigure(id, text=newText)
#     if font != None:
#         _canvas.itemconfigure(id, font=(font, '-%d' % size, style))
#
# def change_color(id, newColor):
#     _canvas.itemconfigure(id, fill=newColor)