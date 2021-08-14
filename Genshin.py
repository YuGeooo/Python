# Genshin Impact
# By YuGeooo 2021.08.14

import numpy as np
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']

for y in [0.08, 0.10, 0.12, 0.14, 0.16]:
    x = []      # 净暴击率
    rate = []   # 装备宗室长剑后的暴击增益

    for j in range(1,101):

        res = 0
        k = 1
    
        x.append(j/100)
        r = x[j-1]

        for i in range(1, 10000):
    
            res = res + k * r / i
    
            k = k * (1-r)
    
            if i < 6 :
                r = x[j-1] + i * y
        
            if r > 1 :
                r = 1

        rate.append(res-x[j-1])
        # print(j, res-x[j-1])
        
    plt.plot(x, rate, label=y)

plt.legend(loc = 'upper right', title = '精炼等级')
plt.xlabel('净暴击率（包含圣遗物，不包含武器）')
plt.ylabel('装备宗室长剑后的暴击率增益')
plt.show()

