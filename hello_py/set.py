# -*- coding: gbk -*-
# Author: style_forever
# Date: 10
# Description: 

# Python 中的集合（Set）是一种无序、可变的数据类型，用于存储唯一的元素。

# 集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。

# 在 Python 中，集合使用大括号 {} 表示，元素之间用逗号 , 分隔。

# 另外，也可以使用 set() 函数创建集合。

# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

# 创建格式：

#!/usr/bin/python3

sites = {'Google', 'Run_oob', 'Facebook', 'Baidu'}

print(sites)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Run_oob' in sites :
    print('Run_oob 在集合中')
else :
    print('Run_oob 不在集合中')


# set可以进行集合运算
a = set('abracadabra')
b = set('abc')

print(a)

print(a - b)     # a 和 b 的差集

print(a | b)     # a 和 b 的并集

print(a & b)     # a 和 b 的交集

print(a ^ b)     # a 和 b 中不同时存在的元素