def overlaps(a_left, a_top, a_right, a_bottom, b_left, b_top, b_right, b_bottom):
    overlaps_sq = False

    # X-AXIS ITERATION
    if (a_left >= b_left and a_left <= b_right) or (a_right >= b_left and a_right <= b_right):
        # Y-AXIS ITERATION
        if (a_top >= b_bottom and a_top <= b_top) or (a_bottom >= b_bottom and a_bottom <= b_top):
            overlaps_sq = True

    # RETURN STATEMENT
    return overlaps_sq


def inside(a_left, a_top, a_right, a_bottom, b_left, b_top, b_right, b_bottom):
    inside_rect = False

    # X-AXIS ITERATION
    if (a_left >= b_left and a_left <= b_right) and (a_right >= b_left and a_right <= b_right):
        # Y-AXIS ITERATION
        if (a_top >= b_bottom and a_top <= b_top) and (a_bottom >= b_bottom and a_bottom <= b_top):
            inside_rect = True

    # RETURN STATEMENT
    return inside_rect


def covers(a_left, a_top, a_right, a_bottom, b_left, b_top, b_right, b_bottom):
    covered = False
    # X-AXIS ITERATION
    if (b_left >= a_left and b_left <= a_right) and (b_right >= a_left and b_right <= a_right):
        # Y-AXIS ITERATION
        if (b_top >= a_bottom and b_top <= a_top) and (b_bottom >= a_bottom and b_bottom <= a_top):
            covered = True

    # RETURN STATEMENT
    return covered