import matplotlib.pyplot as plt
import numpy as np
import random

size = 11
a=50
b=200

plt.figure('Area Plot')

x = [i for i in range(1,size)]

y1 = [random.randint(a,b) for i in range(1,size)]
y2 = [random.randint(a,b) for i in range(1,size)]
y3 = [random.randint(a,b) for i in range(1,size)]
y4 = [random.randint(a,b) for i in range(1,size)]

colors = ['c','m','g','y']
labels = ['y1','y2','y3','y4']

for i in range(4):
    plt.plot([],[],color=colors[i],label=labels[i],linewidth=i+1)

plt.stackplot(x,y1,y2,y3,y4,colors=colors)

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.title('area plotting of random values')
plt.legend()
plt.show()
