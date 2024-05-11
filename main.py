import matplotlib.pyplot as plt
import functions

origin = [12, 10]
# Draw
a1 = plt.plot([15, 12], [10, 10])

b1 = plt.plot([15, 15], [10, 13])

c1 = plt.plot([15, 12], [13, 10])

# Draw Lines
newCoords = functions.getNewLine(c1)
b2 = plt.plot(newCoords[0], newCoords[1])
nCoords = b2[0].get_data()
c2 = plt.plot([nCoords[0][0], origin[0]], [nCoords[1][0], origin[1]])

newCoords = functions.getNewLine(c2)
b3 = plt.plot(newCoords[0], newCoords[1])
nCoords = b3[0].get_data()
c3 = plt.plot([nCoords[0][0], origin[0]], [nCoords[1][0], origin[1]])

newCoords = functions.getNewLine(c3)
b4 = plt.plot(newCoords[0], newCoords[1])
nCoords = b4[0].get_data()
c4 = plt.plot([nCoords[0][0], origin[0]], [nCoords[1][0], origin[1]])

newCoords = functions.getNewLine(c4)
b5 = plt.plot(newCoords[0], newCoords[1])
nCoords = b5[0].get_data()
c5 = plt.plot([nCoords[0][0], origin[0]], [nCoords[1][0], origin[1]])

newCoords = functions.getNewLine(c5)
b6 = plt.plot(newCoords[0], newCoords[1])
nCoords = b6[0].get_data()
c6 = plt.plot([nCoords[0][0], origin[0]], [nCoords[1][0], origin[1]])

newCoords = functions.getNewLine(c6)
b7 = plt.plot(newCoords[0], newCoords[1])
nCoords = b7[0].get_data()
c7 = plt.plot([nCoords[0][0], origin[0]], [nCoords[1][0], origin[1]])

# Make square plot
plt.axis('square')

# Draw to Screen
plt.show()
