import matplotlib.pyplot as plt
import random

a,b = 1,100
size = b//10 + 1
bins = [i*10 for i in range(1,size)]

values = [random.randint(a,b) for i in range(100)]

plt.hist(values,bins,rwidth=0.88)
plt.title('frequency of 200 random values b/w '+str(a)+' and '+str(b))
plt.xlabel('range')
plt.ylabel('frequency')
# plt.grid()

plt.show()
