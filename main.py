import matplotlib.pyplot as plt
import functions
origin = [12, 10]
##A
a1 = plt.plot([15, 12], [10, 10])

##B
b1 = plt.plot([15, 15], [10, 13])

##C
c1 = plt.plot([15, 12], [13, 10])

newCoords = functions.getNewLine(c1)

b2 = plt.plot(newCoords[0], newCoords[1])
nCoords = b2[0].get_data()
c2 = plt.plot([nCoords[0][0],origin[0]], [nCoords[1][0],origin[1]])

newCoords = functions.getNewLine(c2)
b3 = plt.plot(newCoords[0], newCoords[1])
nCoords = b3[0].get_data()
c3 = plt.plot([nCoords[0][0],origin[0]], [nCoords[1][0],origin[1]])

# square plot
plt.axis('square')

##Draw to Screen
plt.show()
