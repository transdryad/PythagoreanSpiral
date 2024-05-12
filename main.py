import matplotlib.pyplot as plt
import functions

origin = [0, 0]


def main():
    # Draw
    plt.plot([3, 0], [0, 0])

    plt.plot([3, 3], [0, 3])

    c1 = plt.plot([3, 0], [3, 0])

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
