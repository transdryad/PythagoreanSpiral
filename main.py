import matplotlib.pyplot as plt
import functions

origin = [12, 10]


def main():
    # Draw
    plt.plot([15, 12], [10, 10])

    plt.plot([15, 15], [10, 13])

    c1 = plt.plot([15, 12], [13, 10])

    # Draw Lines
    newCoords = functions.getNewLine(c1)
    old_triangle = functions.drawNewTriangle(newCoords)

    # Draw new lines in format triangles - 2
    for x in range(0, 5):
        newCoords = functions.getNewLine(old_triangle)
        old_triangle = functions.drawNewTriangle(newCoords)

    # Make square plot
    plt.axis('square')

    # Draw to Screen
    plt.show()


if __name__ == '__main__':
    main()
