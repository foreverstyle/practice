# -*- coding: gbk -*-

# List（列表） 是 Python 中使用最频繁的数据类型。

# 列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。

# 列表是写在方括号 [] 之间、用逗号分隔开的元素列表。

# 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。

# 列表截取的语法格式如下：

#!/usr/bin/python3

list1 = [ 'abcd', 786 , 2.23, 'python', 70.2 ]  # 定义一个列表
list2 = [123, 'python']

print (list1)            # 打印整个列表
print (list1[0])         # 打印列表的第一个元素
print (list1[1:3])       # 打印列表第二到第四个元素（不包含第四个元素）
print (list1[2:])        # 打印列表从第三个元素开始到末尾
print (list2 * 2)    # 打印list2列表两次
print (list1 + list2)  # 打印两个列表拼接在一起的结果

# 与Python字符串不一样的是，列表中的元素是可以改变的
# 第一个是头，第二个是尾，第三个是步长，如果步长为负数，则表示逆序

#list的内置函数
lst = [1, 2, 3]
print(lst.count(2))  # 输出: 1
print(lst.index(2))  # 输出: 1

print(len(lst)) # 输出: 3

print(2 in lst)  # 输出: True
print(4 in lst)  # 输出: False

print(min(lst))  # 输出: 1
print(max(lst))  # 输出: 3
print(sum(lst))  # 输出: 6


lst.append(4)
print(lst)  # 输出: [1, 2, 3, 4]

lst.extend([4, 5])
print(lst) #    输出: [1, 2, 3, 4, 4, 5]

lst.insert(1, "a")
print(lst)  # 输出: [1, 'a', 2, 3, 4, 4, 5]

lst.remove(2)
print(lst)  # 输出: [1, 'a', 3, 4, 4, 5]    移除第一个2

lst.pop()
print(lst)  # 输出: [1, 'a', 3, 4, 4]   删除最后一个元素

lst.pop(1)
print(lst)  # 输出: [1, 3, 4, 4]    删除第二个元素

lst.reverse()
print(lst)  # 输出: [4, 4, 3, 'a', 1]

lst.sort()
print(lst)  # 输出: [1, 3, 4, 4, 'a']  



# 导入 operator 模块
import operator

a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a,b))
print("operator.eq(c,b): ", operator.eq(c,b))

# list() 是用于创建列表的内置函数。它可以将可迭代对象（如字符串、元组、字典等）转换为列表，或者创建一个空列表。

# 语法格式如下：
# 创建空列表
empty_list = list()
print(empty_list)  # Output: []

# 将字符串转换为列表
str_list = list("hello")
print(str_list)  # Output: ['h', 'e', 'l', 'l', 'o']

# 将元组转换为列表
tuple_list = list((1, 2, 3))
print(tuple_list)  # Output: [1, 2, 3]

