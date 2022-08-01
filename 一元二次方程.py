# Python 求解一元二次方程
# By Yun
# 2022.07.24

import math

# 知识点：连续输入多个 float 型数字
a,b,c = map(float,input("对于方程a^2x+bx+c=0, \n请输入a,b,c(空格隔开):").split())
# Tips: 可以通过.split(',') 将输入的分隔符改为逗号

k = b*b-4*a*c

# 知识点：if 判断语句的使用
if k < 0 :
    print('方程无解')

# 注意，逻辑'等于'是两个等号，一个等号代表赋值
elif k == 0 :
    x = -b/(2*a)

    # 知识点：通过 %.2f 使输出的数保留两位小数
    print('方程的解为：x1=x2=%.2f' % x)

else :
    x1 = (-b+math.sqrt(k))/(2*a)
    x2 = (-b-math.sqrt(k))/(2*a)

    # 知识点：如何将文字和多个变量混合输出?
    print('\n方程的解为: x1=%.2f, x2=%.2f' % (x1,x2))