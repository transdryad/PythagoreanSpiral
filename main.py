import matplotlib.pyplot as plt
import functions
origin = [10, 12]
##A
a1 = plt.plot([15, 12], [10, 10])

##B
b1 = plt.plot([15, 15], [10, 13])

##C
c1 = plt.plot([15, 12], [13, 10])

newCoords = functions.getNewLine(c1)

b2 = plt.plot(newCoords[0], newCoords[1])

# square plot
plt.axis('square')

##Draw to Screen
plt.show()
