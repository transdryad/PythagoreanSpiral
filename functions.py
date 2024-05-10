import numpy
import math


def getNewLine(oldLine):
    coords = oldLine[0].get_data()
    print(coords)

    x1 = coords[0][0]
    x2 = coords[0][1]
    y1 = coords[1][0]
    y2 = coords[1][1]

    m = (y2 - y1) / (x2 - x1)

    m2 = numpy.reciprocal(m)

    m3 = m2 * -1
    print(m)
    print(m2)
    print(m3)
    slopeAngle = math.degrees(math.atan(m3))
    print(slopeAngle)
    angle = slopeAngle
    print(angle)

    offset_x = math.cos(angle) * 3
    print(offset_x)
    offset_y = math.sin(angle) * 3
    print(offset_y)

    x2 = x1 - offset_x
    x = [x2, x1]
    y2 = y1 - offset_y
    y = [y2, y1]
    return [x, y]
