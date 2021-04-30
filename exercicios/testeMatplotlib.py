import matplotlib. pyplot as plt
from numpy import random

histA = random.randint(1000,50000, size=(350))
histB = sorted(histA)

#print(len(b))
#print(b)

plt.hist(histB)
plt.show()
