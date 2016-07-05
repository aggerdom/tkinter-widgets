import math

def in_circle(x_offset, y_offset, radius):
    """Returns true or false"""
    la = x_offset #length a
    lb = y_offset #length b
    lc = math.sqrt(la**2 + lb**2) #hypotenus length
    if lc <= radius:
        return True
    else:
        return False


def is_inside_circle(center_x, center_y, radius, point_x, point_y):
    x_offset = abs(center_x - point_x)
    y_offset = abs(center_y - point_y)
    answer = in_circle(x_offset, y_offset, radius)
    return answer

