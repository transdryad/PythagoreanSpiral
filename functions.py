import numpy
import math
import matplotlib.pyplot as plt

origin = [0, 0]


def getNewLine(oldLine):
    # Get coordinates of start and end of old line.
    coords = oldLine[0].get_data()
    ncoords = str(coords)
    print("Old Coordinates: " + ncoords)
    # Store Coordinates in variables.
    x1 = coords[0][0]
    x2 = coords[0][1]
    y1 = coords[1][0]
    y2 = coords[1][1]
    # Calculate slope of the old line.
    m = (y2 - y1) / (x2 - x1)
    # Get perpendicular slope.
    m2 = numpy.reciprocal(m)
    m3 = m2 * -1
    m = str(m)
    m2 = str(m2)
    m4 = str(m3)
    print("Slope of old line: " + m)
    print("Reciprocal of that: " + m2)
    print("Slope perpendicular to old line: " + m4)
    # Change Slope into Degrees from x-axis.
    angle = math.atan(m3)
    nangle = str(angle)
    print("Angle perpendicular to old line: " + nangle)
    # Take the imaginary triangle's side lengths from angle and length of hypotenuse: 3.
    offset_x = math.cos(angle) * 3
    noffset_x = str(offset_x)
    print("Offset x: " + noffset_x)
    offset_y = math.sin(angle) * 3
    noffset_y = str(offset_y)
    print("Offset y: " + noffset_y)
    # Use distance from endpoint of last line to calculate final x/y for new line.
    x2 = x1 - offset_x
    x = [x2, x1]
    y2 = y1 - offset_y
    y = [y2, y1]
    # Send back the x and y to main drawing file.
    return [x, y]


# Draw new triangle from recently created coords.
def drawNewTriangle(coords):
    b2 = plt.plot(coords[0], coords[1])
    n_coords = b2[0].get_data()
    c2 = plt.plot([n_coords[0][0], origin[0]], [n_coords[1][0], origin[1]])
    return c2
