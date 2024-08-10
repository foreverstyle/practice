# -*- coding: gbk -*-
# Author: style_forever
# Date: 09
# Description: 

#!/usr/bin/python3

tuple = ( 'abcd', 786 , 2.23, 'python', 70.2  )
tiny_tuple = (123, 'python')

print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tiny_tuple * 2)     # 输出两次元组
print (tuple + tiny_tuple) # 连接元组