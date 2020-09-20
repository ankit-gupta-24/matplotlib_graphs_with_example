import matplotlib.pyplot as plt
import numpy as np

plt.figure('Line Plot')
plt.title('Line Plot')
plt.ylabel('y-axis')
plt.xlabel('x-axis')

x = [1,2,3,4,5]

y1 = [20,30,40,50,30]
y2 = [22,44,33,11,22]
y3 = [9,4,22,5,45]

plt.plot(x,y1,'g',label='y1',linewidth=3)
plt.plot(x,y2,'r',label='y2',linewidth=3)
plt.plot(x,y3,'b',label='y3',linewidth=2)
plt.legend() #shows color indicator with label
plt.grid()
plt.show()
