import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import random

a=1
b=5
size = 6
x= [i for i in range(1,size)]

arr = [random.randint(a,b) for i in range(100)]
arr_freq = dict(Counter(arr))

blocks=[]
for i in range(1,size):
    blocks.append(arr_freq[i])

labels = [str(i)+' ('+str(blocks[i-1])+')' for i in range(1,size)]

colors = ['c','m','g','b','r']
explode = [0 for i in range(1,size)]
explode[1] = 0.1 

plt.figure('Pie Plot')
plt.title('Frequency of 100 random values b/w 1 and 5')

plt.pie(blocks,labels=labels,colors=colors,startangle=45,shadow=True,explode=explode,autopct='%1.1f%%')

plt.show()


