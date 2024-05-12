import matplotlib.pyplot as plt
import functions

origin = [12, 10]
# Draw
a1 = plt.plot([15, 12], [10, 10])

b1 = plt.plot([15, 15], [10, 13])

c1 = plt.plot([15, 12], [13, 10])

# Draw Lines
newCoords = functions.getNewLine(c1)
old_triangle = functions.drawNewTriangle(newCoords)

for x in range(0, 4):
    newCoords = functions.getNewLine(old_triangle)
    old_triangle = functions.drawNewTriangle(newCoords)

# Make square plot
plt.axis('square')

# Draw to Screen
plt.show()
