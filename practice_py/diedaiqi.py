# -*- coding: gbk -*-
# Author: style_forever
# Date: 11
# Description: 


# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

# 迭代器有两个基本方法：iter() 和 next()。
# iter() 方法返回一个迭代器对象，next() 方法则返回下一个元素。
# 
# 我们可以使用 iter() 函数获取一个迭代器对象，然后使用 next() 函数不断获取下一个元素。
# 
# 例如，我们可以使用 range() 函数创建一个迭代器：


r = range(5)
print(r)  # range(0, 5)

it = iter(r)
print(it)  # <range_iterator object at 0x000001>

print(next(it))  # 0
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # 4

# 由于迭代器只能往前不会后退，所以我们无法使用 prev() 函数获取上一个元素。
# 
# 但是，迭代器可以被重新初始化，因此我们可以多次遍历同一个序列：



#!/usr/bin/python3
 
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x)



#迭代器
class CountToN:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

# 使用迭代器
counter = CountToN(5)

for number in counter:
    print(number)




#生成器
def countdown(n):
    while n > 0:
        yield n     #相当于迭代，return，但是不会立即结束，而是返回一个生成器对象
        n -= 1
 
# 创建生成器对象
generator = countdown(5)  #生成iter对象 
 
# 通过迭代生成器获取值
print(next(generator))  # 输出: 5
print(next(generator))  # 输出: 4
print(next(generator))  # 输出: 3
 
# 使用 for 循环迭代生成器
for value in generator:
    print(value)  # 输出: 2 1