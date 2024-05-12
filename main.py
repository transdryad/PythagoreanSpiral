import matplotlib.pyplot as plt
import functions

origin = [30, 30]


def main():
    # Draw
    x = 1
    plt.plot([33, 30], [30, 30])

    plt.plot([33, 33], [30, 33])

    c1 = plt.plot([33, 30], [33, 30])

    # Draw Lines
    newCoords = functions.getNewLine(c1, x)
    old_triangle = functions.drawNewTriangle(newCoords)

    # Draw new lines in format triangles - 2
    for x in range(0, 5):
        newCoords = functions.getNewLine(old_triangle, x)
        old_triangle = functions.drawNewTriangle(newCoords)

    # Make square plot
    plt.axis('square')

    # Draw to Screen
    plt.show()


if __name__ == '__main__':
    main()
