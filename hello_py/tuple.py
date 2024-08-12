# -*- coding: gbk -*-
# Author: style_forever
# Date: 09
# Description: 

#!/usr/bin/python3

tuple1 = ( 'abcd', 786 , 2.23, 'python', 70.2  )
tiny_tuple = (123, 'python')

print (tuple1)             # 输出完整元组
print (tuple1[0])          # 输出元组的第一个元素
print (tuple1[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple1[2:])         # 输出从第三个元素开始的所有元素
print (tiny_tuple * 2)     # 输出两次元组
print (tuple1 + tiny_tuple) # 连接元组

# 可以把字符串看作一种特殊的元组。字符串的每个字符就是元组的一个元素。因此，字符串也可以被索引和切片。

# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。与字符串一样，元组的元素不能修改。

# 创建空元组：
empty_tuple = tuple()
print(empty_tuple)  # Output: ()

# # 从列表创建元组：
tuple_from_list = tuple([1, 2, 3])
print(tuple_from_list)  # Output: (1, 2, 3)

# # 从字符串创建元组：
tuple_from_str = tuple("hello")
print(tuple_from_str)  # Output: ('h', 'e', 'l', 'l', 'o')

