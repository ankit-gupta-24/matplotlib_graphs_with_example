import matplotlib.pyplot as plt
import numpy as np

# It is a diagram or a shape that can be formed by a collection of plots in different dimensions.
plt.figure('Line Plot')
# It is used to display the title of the graph.
plt.title('Graph') 
# It is used to add labels or names to respective x and y axes.
plt.xlabel('x-axis')
plt.ylabel('y-axis')
# It is a collection of objects and functions which is concerned with 3-dimensional data.
plt.grid()

# A subplot() function can be called to plot multiple plots in the same figure.
# subplot :firstArg -> no. of rows, secondArg -> no. of cols, thirdArg -> 1<= thirdArg <=rows*cols
plt.subplot(3,3,5)
# Plot():It is an illustration that can be represented using a graph.
# here the list in plot argument represent y values corresponding to x=[0,1,2,3,4,5,6,...]
plt.plot([1,2,1,2]) 

plt.subplot(3,3,4)
plt.plot([1,1])

plt.subplot(3,3,2)
plt.plot([1,3,1])

plt.show()

