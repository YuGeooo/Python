import numpy as np
import matplotlib.pyplot as plt
import math

list = ([],[],[],[])
plt.figure(1)

for n in range(1,5):
    for x in np.arange(0,1,0.001):
        list[n - 1].append(math.sin(n * math.pi * x))
    plt.plot(np.arange(0,1,0.001),list[n-1], label = n)
    
plt.xlabel('X', fontsize = 15)
plt.ylabel('Y', fontsize = 15)
plt.title('Y = sin nπx', fontsize = 25)
plt.legend(bbox_to_anchor=(1.17,1),
           title = 'n')
plt.show()