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

# 集合的内置函数

print(len(sites))  # 集合的元素个数

print(sites.add('Tao_bao'))  # 向集合中添加元素

print(sites)

print(sites.remove('Tao_bao'))  # 从集合中删除元素

print(sites)

print(sites.pop())  # 随机删除集合中的一个元素

print(sites)

print(sites.clear())  # 清空集合

print(sites)


# 创建空集合
empty_set = set()
print(empty_set)  # Output: set()

# 从列表或其他可迭代对象创建集合：
set_from_list = set([1, 2, 2, 3, 4])
print(set_from_list)  # Output: {1, 2, 3, 4}  (重复的元素被自动去除)

# 从字符串创建集合：
set_from_str = set("hello")
print(set_from_str)  # Output: {'h', 'e', 'l', 'o'}

