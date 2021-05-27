# Python 基础语法



### 输入输出

```python
# input 输入
str1 = input("提示字符信息串")

# print 输出
print ("CONTEXT")
print x
print x,		# 不换行输出
print x,y

# format 函数
# 1
print("学校：{uni}, 地址 {adr}".format(uni = "中国地质大学", adr = "湖北武汉"))
# 2
site = {"uni": "中国地质大学", "adr": "湖北武汉"}	# 通过字典设置参数
print("学校：{uni}, 地址 {adr}".format(**site))

# 三引号可以跨越多行输出文本
a = '''
Line 1
Line 2
Line 3
'''

```



### 字符串的格式化

：【填充】【对齐】【宽度】【,】【.精度】【类型】

|  符号   |           描述           |    例     |
| :-----: | :----------------------: | :-------: |
|   %d    |      格式化**整数**      |           |
|   %f    |   格式化**浮点型数字**   |           |
|   %c    |      格式化**字符**      |           |
|   %s    |     格式化**字符串**     |           |
| {:.2f}  |     保留小数点后两位     |   3.14    |
|  {:,}   |    大数以逗号形式分隔    | 1,000,000 |
| {:.2e}  |  指数记法，保留两位小数  |  1.00e+9  |
| {:.2%}  | 百分比格式，保留两位小数 |  25.00%   |
| {:^10d} |    居中对齐，宽度为10    |           |
| {:>10d} |     右对齐，宽度为10     |           |
| {:<10d} |     右对齐，宽度为10     |           |
|         |                          |           |



### 转义字符，字符串操作符

|     符号     |               描述               |
| :----------: | :------------------------------: |
|      \n      |       换行，光标移到本行首       |
|      \r      |          光标移到下行首          |
|      \b      |        回退（Backspace）         |
| str1 + str2  |          连接两个字符串          |
| str1 in str2 | str1 是 str2 的子串，则返回 True |
|   len( x )   |          返回字符串长度          |
|   eval( )    |        去掉参数最外侧引号        |
|              |                                  |



### If - else 结构

```python
if expression :
    suite
elif expression :
    suite
else :
    suite
    
pass # 空语句，为了保持程序结构的完整性

if a in [ ]
```



### 循环结构

```python
# While 循环
while condition :
    statements...
    
# for 循环
for interating_var in sequence : 
    statements...
# 例如：
for i in range(10):
    ...
for word in list1:
    ...
for key in dict1:
    ...
    
# 循环控制保留字    
break    # 跳出当前层次循环
continue # 跳过本次循环，进行下一遍循环

# range 函数
range(start, stop[, step])	# 返回一个序列的数，常用于循环，step 默认 1
for i in range(10)	  		# 共 10 个，从 1 - 10 
for i in range(1, 10) 		# 共  9 个，左闭右开
```



### 列表 List

```python
# 新建列表
list1 = [1234, 'abcd']

# 引用列表中元素（方括号）
list1[0]
list1[1:5]

list1.append('HelloWorld')	# 在列表末尾添加元素
list1.insert(index, boj)	# 在列表中添加元素
list1 + list2				# 合并列表

# 删除列表中的元素
del list1[1]
list1.clear( )

# 列表元素个数
len(list1)

# 列表元素的最大（小）值
max(list1)
min(list1)

# 反向列表中的元素
list1.reverse( )

# 列表中元素排序
list1.sort(cmp = None, key = None, reverse = False)
	# reverse = False 升序
    # reverse = Ture  降序
	# key	  用来比较的元素
    	# 利用匿名函数 lambda 来比较二维列表里的子项
    	# 例如：key = lambda x:x[1]
    
# 元组 tuple与列表类似，但元组中元素不能修改，用圆括号
tup1()
```



### 字典 Dictionary

```python
# 新建字典
dict1 = {key1 : value1, key2 : value2}

# 访问字典里的值
dict1[key1]

# 修改/填加字典
dict1[key1] = value3    

# 删除字典
del dict1[key1]
dic1t.clear( )	# 清除字典里所有条目

# 字典中元素个数
len(dect1)

# 字典中键不可变，不可重复

```



### 字符串、列表等下标

[Start : End]（**左闭右开**）

|  H   |  E   |  l   |  l   |  o   |
| :--: | :--: | :--: | :--: | :--: |
|  0   |  1   |  2   |  3   |  4   |
|  -5  |  -4  |  -3  |  -2  |  -1  |



### 逻辑运算

| 运算符       | 描述                                            |
| :----------- | :---------------------------------------------- |
| ==  !=       | 等于  不等于                                    |
| >  <  >=  <= |                                                 |
| x  and  y    | 逻辑 “与”                                       |
| x  or  y     | 逻辑 “或”                                       |
| not  x       | 逻辑 “非”                                       |
| x  in  y     | 如果在指定的序列中找到值，返回 True，否则 False |
| x  not in  y | 与 in 相反                                      |
|              |                                                 |



### 数学运算

| 运算符                  | 描述                   |
| ----------------------- | ---------------------- |
| +  -  *  /              |                        |
| **                      | 幂                     |
| //    %                 | 取整（向下取整）；取余 |
| abs( )                  | 返回数字的绝对值       |
| exp( )                  | 返回 e 的(...)次幂     |
| sqrt( )                 | 返回数字的平方根       |
| min( )  max( )          |                        |
| log( )   log10( )       |                        |
| sin( )  cos( )  tan(  ) |                        |
| pi    e                 | 数字常量               |
|                         |                        |



### 函数

```python
# 定义一个函数
def functionname( parameters )
	"函数说明"
    function_suit
    return[ expression ]

# numbers, strings, tuples 是不可更改对象
# list, dict	 		   是可更改对象

# 不定长参数
def functionname(var1, *varls) # 加 * 的变量会存放所有未命名的变量参数
```



### 模块

```python
# 引入模块
import module1
import module1 as m # 起个简单的别名
import modulel as * # 省略其名称

# 调用模块中的函数
module1.function1( )

# 引入模块中一部分
from module1 import function1

# 模块的搜索路径为：当前目录、shell 下 pythonpath、默认路径

# 全局变量
global var1

# 模块中所有定义过的名字
dar( module1 )

# 重新导入模块
reload( module1 )
```



### 文件

```python
# 打开文件
file1 = open("file_name", "access_mode", buffering = -1, encoding = None)
	# access_mode 打开文件的模式
    # buffering   寄存区的缓冲大小
    # encoding    编码方式，一般用 utf8

with open(...) as file1
#使用 with 后不管 with 中的代码出现什么错误，都会进行对当前对象进行清理工作，
#例如 file 的 file.close()，无论 with 中出现任何错误，都会执行 file.close() 


file1.closed # 文件已被关闭则返回 Ture
file1.mode   # 返回文件的访问模式
file1.name	 # 返回文件名

# 关闭文件
file1.close( )

# 文件中写入
file1.write( "CONTEST" )
file1.writelines( lines )	#逐行写入

# 读取文件
file1.read( count )			# count 读取的字节数；默认读取全部
file1.readlines( lines )	# 逐行读取
	# 默认一次读取文件所有行，每行作为一个元素构成一个 list

# 文件定位
file1.seek(offset)
	# offset = 0 文件开头
	# offset = 1 当前位置
	# offset = 2 文件结尾

# os文件操作
import os
os.rename(current_filename, new_filename)	# 重命名文件
os.remove( filename )	# 删除文件
os.mkdir( dirname )		# 创建目录	
os.chdir( new_dirname )	# 更改当前目录名
os.rmdir( dirname )		# 删除目录
os.getcwd( )			# 当前工作目录

```



### 一、二维数据的读写处理

```python
# 两个重要的函数
.split( )
.join( )

# 一维文件读写
list1 = file1.split( )					# 从空格分隔的文件中读取数据
list1 = file1.split(",")				# 从逗号分隔的文件中读取数据
list1 = file1.write(' '.join(list1) )
list1 = file1.write(','.join(list1) )

# 从二维文件（.csv）中读入数据
file1 = open(filename)
list1 = []
for line in file1
	line = line.replace("\n", "")
    list1.append(line.split(",") )
file1.close()

# 数据写入到.csv中
list1 = [[], [], []]	# 二维列表
file1 = open(filename)
for item in list1
	file1.write(','.join(item) + '\n')
file1.close()
```



### 打开文件的模式

| 模式 |         描述         |
| :--: | :------------------: |
|  t   |   文本模式（默认）   |
|  r   |         只读         |
|  rb  |     二进制，只读     |
|  r+  | 读写，文件指针在开头 |
| rb+  |      二进制读写      |
|  w   |         只写         |
|  wb  |      二进制只写      |
|  w+  | 读写，会覆盖原有内容 |
|  a   | 追加，文件指针在结尾 |
|  a+  | 读写，文件指针在结尾 |
|      |                      |



### Turtle 绘图

```python
import turtle

# 画笔控制函数
turtle.penup()		# 抬起画笔
turtle.pendown()	# 落下画笔

turtle.pensize(width)	# 画笔宽度
turtle.hideturtle	# 隐藏画笔箭头

turtle.pencolor("color")	# 画笔颜色
turtle.fillcolor("color")	# 填充颜色
turtle.begin_fill()	# 开始填充颜色
turtle.end_fill()	# 结束填充颜色

#运动控制函数
turtle.forward(distance)	# 画笔直线行进（距离）
trutle.circle(r, degree)	# 画笔弧线行进（半径，角度）

turtle.seth(angle)			# 画笔改变行进方向（绝对角度，逆时针方向）
turtle.left(angle)			# 画笔左转（相对角度）
turtle.right(angle)			# 画笔右转（相对角度）

```



### Jieba 中文语料分词

```python
import jieba

# cut_all = False 精确模式（默认）
# cut_all = True  全模式

# jieba.cut 需要 .join 来输出，可以自定义分隔符
seg_list = jieba.cut("str", cut_all = False)
print(", " .join(seg_list) )

# jieba.lcut 直接生成一个 list
seg_list = jieba.lcut("str", cut_all = False)
print(seg_list)


# 词频统计问题 #

# 1.读取句子
# 2.分词
	txt = jieba.lcut(sentence, cut_all = True)
# 3.构建字典统计词频
	dict1 = {}
	for word in txt:
    	if word not in dict1:
        	dict1[word] = 1
    	else：
    		dict1[word] += 1 
# 4.字典转换为列表
	list1 = (dict1.items())
# 5.根据词频排序
	list1.sort(key = lambda x:x[1], reverse = True)
# 6.输出
	for block in list1
    	print("{}:{}".format(block[0], block[1]))
```



### Python 常用库

|                  |                        |                       |                                 |
| :--------------: | :--------------------: | :-------------------: | :-----------------------------: |
|    **标准库**    | turtle \| 基本图形绘制 |   random \| 随机数    |        time \| 时间功能         |
|   **中文分词**   |         jieba          |       wordcloud       |                                 |
|   **网络爬虫**   |  requests \| HTTP处理  | scrapy \| Web获取框架 |    pyspider \| 抓取环境模型     |
|   **数据分析**   |   numpy \| 多维数组    |  pandas \| 数据分析   |        scipy \| 科学计算        |
|   **文本处理**   |        pdfminer        |      python-docx      | beautifulsoup4 \| HTML、XML提取 |
|  **数据可视化**  | matplotlib \| 数学绘图 |        seaborn        |       mayavi \| 三维绘图        |
| **用户图形界面** |         PyQt5          |       wxPython        |              pyGTK              |
|   **机器学习**   |      scikit-learn      |      TensorFlow       |              mxnet              |
|   **Web 开发**   |         Django         |        Pyramid        |              flask              |
|   **游戏开发**   |         Pygame         |        Panda3D        |             cocos2d             |
|                  |                        |                       |                                 |

