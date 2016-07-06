import math
from collections import namedtuple

"""
Various functions for things like finding line intersections, useful for when doing stuff with the canvas
"""


def intersects(a1, a2, b1, b2):
    """
    Given x,y coordinates for four points defining two lines,
    returns false if lines don't intersect
    else returns thier intersection.
    # http://stackoverflow.com/questions/3746274/line-intersection-with-aabb-rectangle
    """
    vector = namedtuple("vector", ["X", "Y"])
    a1, a2, b1, b2 = vector(*a1), vector(*a2), vector(*b1), vector(*b2)
    b = vector(a2.X - a1.X,
               a2.Y - a1.Y)
    d = vector(b2.X - b1.X,
               b2.Y - b1.Y)
    bDotDPerp = b.X * d.Y - b.Y * d.X

    # if b dot d == 0, it means the lines are parallel
    # so have infinite intersection points
    if bDotDPerp == 0:
        return False

    c = vector(b1.X - a1.X,
               b1.Y - a1.Y)
    t = (c.X * d.Y - c.Y * d.X) / bDotDPerp  # float

    if (t < 0 or t > 1):
        return False

    u = (c.X * b.Y - c.Y * b.X) / bDotDPerp  # float
    if (u < 0 or u > 1):
        return False
    intersection = vector(a1.X + t * b.X,
                          a1.Y + t * b.Y)
    return intersection


def calc_intersect_ray_rectangle(pointx, pointy, rectcenterx, rectcentery, rectwidth, rectheight):
    """
          A ---------------- B
          |    rectcenter    |
          C ---------------- D
    """
    minX = rectcenterx - .5 * rectwidth
    minY = rectcentery - .5 * rectheight
    maxX = rectcenterx + .5 * rectwidth
    maxY = rectcentery + .5 * rectheight

    A = minX, minY
    B = maxX, minY
    C = minX, maxY
    D = maxX, maxY

    intAB = intersects((pointx, pointy), (rectcenterx, rectcentery), A, B)
    intAC = intersects((pointx, pointy), (rectcenterx, rectcentery), A, C)
    intBD = intersects((pointx, pointy), (rectcenterx, rectcentery), B, D)
    intCD = intersects((pointx, pointy), (rectcenterx, rectcentery), C, D)
    for possibleIntersection in (intAB, intAC, intBD, intCD):
        if possibleIntersection is not False:
            return possibleIntersection.X, possibleIntersection.Y
    return None


def in_circle(x_offset, y_offset, radius):
    """Returns true or false"""
    la = x_offset  # length a
    lb = y_offset  # length b
    lc = math.sqrt(la ** 2 + lb ** 2)  # hypotenus length
    if lc <= radius:
        return True
    else:
        return False


def is_inside_circle(center_x, center_y, radius, point_x, point_y):
    x_offset = abs(center_x - point_x)
    y_offset = abs(center_y - point_y)
    answer = in_circle(x_offset, y_offset, radius)
    return answer
