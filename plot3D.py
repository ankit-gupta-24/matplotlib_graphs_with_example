import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')


a,b=50,100
size = 6

x = [i for i in range(1,size)]

y = [ [random.randint(a,b) for i in range(1,size)] for i in range(4)]

labels = ['y1','y2','y3','y4']
colors = ['r','g','b','m']

for i in range(4):
    plt.plot(x,y[i],label=labels[i],color=colors[i])

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Generating Random Values b/w '+str(a)+' & '+str(b)+' 4 times')

plt.legend()
plt.show()