
# I modified it slightly from the slide in order to avoid using
# camel case for a function which would violate Python conventions
# established in PEP 8.

def draw_line(x1: int, y1: int, x2:int, y2:int) -> bool:

    line_width = 2
    color = "black"

    # code which draws a line.
    # ...
    print("Drawing %s line (%d, %d)-(%d, %d) with width=%d\n" % (
        color, x1, y1, x2, y2, line_width))
    return True


def draw_square(x1: int, y1: int, x2:int, y2:int):
    # should really be called "draw_rect", but I don't want to
    # update all the slides.

    # draw top
    success = draw_line(x1, y1, x2, y1)
    if not success:
        raise Exception("Some exception")

    # draw left side
    success = draw_line(x1, y1, x1, y2)
    if not success:
        raise Exception("Some exception")

    # draw right side
    draw_line(x2, y1, x2, y2)
    if not success:
        raise Exception("Some exception")

    # draw bottom
    draw_line(x1, y2, x2, y2)
    if not success:
        raise Exception("Some exception")

draw_square(10, 20, 30, 40)
