import tkinter as tk
import math

window = tk.Tk()
window.title('一元二次方程计算器')
# window.geometry('800x400') # 可以指定窗口的大小

# 一些界面元素
# grid 是一个格点，决定元素显示哪里
# columnspan 横跨多列格点，rowspan 同理
# padx pady ipadx ipady 调整分别调整外边距和内边距
# sticky = E 靠右 W 靠左

k = tk.Label(window,text='请输入一元二次方程的参数:',font=('Arial',12)) # 文字label
k.grid(row=0,column=0,columnspan=3,sticky='w',padx=10,pady=10)

x02 = tk.Entry(window) # 输入框
x02.grid(row=1,column=0,padx=10)

p1 = tk.Label(window,text=' x^2 + ',font=('Arial',12))
p1.grid(row=1,column=1)

x01 = tk.Entry(window)
x01.grid(row=1,column=2)

p2 = tk.Label(window,text=' x + ',font=('Arial',12))
p2.grid(row=1,column=3)

x00 = tk.Entry(window)
x00.grid(row=1,column=4)

p3 = tk.Label(window,text=' = 0',font=('Arial',12))
p3.grid(row=1,column=5)

# 一元二次方程计算函数（点击按钮后执行）
def cal():
    a = float(x02.get())
    b = float(x01.get())
    c = float(x00.get())

    k = b*b-4*a*c
    g = -c/b

    if a == 0:
        resu.set('方程的解为: x = %.2f' % g)

    if k < 0 :
        resu.set('方程无解')

    elif k == 0 :
        x = -b/(2*a)
        resu.set('方程的解为: x1 = x2 = %.2f' % x)

    else :
        x1 = (-b+math.sqrt(k))/(2*a)
        x2 = (-b-math.sqrt(k))/(2*a)
        resu.set('方程的解为: x1 = %.2f   x2 = %.2f' % (x1,x2))
    
# 按钮
b1 = tk.Button(window,text='计算',width=10,command=cal)
b1.grid(row=1,column=6,padx=20)

# 结果显示
resu = tk.StringVar() # 字符串变量
l = tk.Label(window,textvariable=resu,font=('Arial',12))
l.grid(row=3,column=0,sticky='w',columnspan=3,padx=10)

window.mainloop()

# 参考资料
# https://blog.csdn.net/muzihuaner/article/details/106248343
# https://www.cnblogs.com/ruo-li-suo-yi/p/7425307.html
# https://www.delftstack.com/zh/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/