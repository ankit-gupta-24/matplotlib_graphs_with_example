import matplotlib.pyplot as plt
import numpy as np
import random
from collections import Counter

plt.figure('Bar char plot')
plt.title('Comparing frequency of 100 random values b/w 1 & 10 generated twice')
plt.xlabel('random value')
plt.ylabel('frequency')


# generating 100 random values b/w 1 and 10
arr= [random.randint(1,10) for i in range(100) ]
# counting frequency
arr_freq = dict(Counter(arr))

x= [i for i in range(1,11)]
y=[]
for i in x:
    y.append(arr_freq[i])

plt.bar(x,y,label='frequency 1',color='b',width=0.3)

arr= [random.randint(1,10) for i in range(100) ]
arr_freq = dict(Counter(arr))


y=[]
for i in x:
    y.append(arr_freq[i])
x= [i+0.4 for i in range(1,11)]

plt.bar(x,y,label='frequency 2',color='r',width=0.3)

plt.legend()
plt.show()