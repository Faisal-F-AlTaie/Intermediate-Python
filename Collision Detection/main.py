def overlaps(a_left, a_top, a_right, a_bottom, b_left, b_top, b_right,
             b_bottom):  # Does rectangle A overlap rectangle B?

    r1 = [a_left, a_top, a_right, a_bottom]  # Rectangle A properties
    r2 = [b_left, b_top, b_right, b_bottom]  # Rectangle B properties

    # Properties of rectangle A compared to rectangle B in a way they overlap
    if (r1[0] <= r2[2]) and (r1[2] >= r2[0]) and (r1[1] >= r2[3]) and (r1[3] <= r2[1]):
        # if rectangles overlap
        return True


    else:

        # if rectangles don't overlap
        return False


# Is rectangle A inside rectangle B?
def inside(a_left, a_top, a_right, a_bottom, b_left, b_top, b_right, b_bottom):
    # Rectangle A properties
    r1 = [a_left, a_top, a_right, a_bottom]

    # Rectangle B properties
    r2 = [b_left, b_top, b_right, b_bottom]

    # Properties of rectangle A compared to rectangle B in way where A is inside B

    if (r1[0] > r2[0]) and (r1[1] < r2[1]) and (r1[2] < r2[2]) and (r1[3] > r2[3]):
        # If A is inside B
        return True
    else:

        # If A is not inside B
        return False

        # Does rectangle A cover rectangle B?


def covers(a_left, a_top, a_right, a_bottom, b_left, b_top, b_right, b_bottom):
    # Rectangle A properties
    r1 = [a_left, a_top, a_right, a_bottom]

    # Rectangle B properties
    r2 = [b_left, b_top, b_right, b_bottom]

    # Properties of rectangle A compared to rectangle B in a way where A covers B
    if (r1[0] < r2[0]) and (r1[1] > r2[1]) and (r1[2] > r2[2]) and (r1[3] < r2[3]):
        return True  # if A covers B

    else:
        return False  # if A does not cover B