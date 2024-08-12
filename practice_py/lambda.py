# -*- coding: gbk -*-
# Author: style_forever
# Date: 12
# Description: 

# Python 使用 lambda 来创建匿名函数。

# 所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。

# lambda 只是一个表达式，函数体比 def 简单很多。
# lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
# lambda [arg1 [,arg2,.....arg]]:expression

# 1. 有参数的匿名函数
# 定义一个求两个数之和的匿名函数：

sum = lambda a, b: a + b
print(sum(1, 2))  # 输出 3

# 2. 无参数的匿名函数
# 定义一个输出 "hello world" 的匿名函数：


hello = lambda: print("hello world")
hello()  # 输出 hello world

# 3. 匿名函数作为参数
# 定义一个求列表中所有元素的平方的匿名函数：

square = lambda x: x ** 2
print(list(map(square, [1, 2, 3, 4, 5])))  # 输出 [1, 4, 9, 16, 25]

# 4. 匿名函数作为返回值
# 定义一个求两个数之商的匿名函数：

division = lambda a, b: a / b
print(division(10, 3))  # 输出 3.3333333333333335


# lambda 函数通常与内置函数如 map()、filter() 和 reduce() 一起使用，以便在集合上执行操作。例如：

# 5. 匿名函数作为内置函数的参数
# 定义一个求列表中所有元素的平方的匿名函数，并作为 map() 函数的参数：

squares = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
print(squares)  # 输出 [1, 4, 9, 16, 25]