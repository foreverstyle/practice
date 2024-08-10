# -*- coding: gbk -*-
# Python允许你同时为多个变量赋值。例如：

a = b = c = 1
print(a,b,c) # Output: 1 1 1

a, b, c = 1, 2, "python"
print(a, b, c) # Output: 1 2 python

a, b, c = 5, 6, 7
print(a / b)
print(a // b)
print(a % b)
print(a ** b)



#数学函数
import math

print(math.sqrt(16))  # Output: 4.0
print(math.pow(2, 3))  # Output: 8.0

print(math.floor(3.7))  # Output: 3 下取整
print(math.ceil(3.2))  # Output: 4 上取整
print(round(3.2))  # Output: 3 四舍五入

print(math.exp(2))  # Output: 7.38905609893065

print(math.log(10))  # Output: 2.302585092994046  默认以e为底
print(math.log(10, 10))  # Output: 1.0 第二个参数是底数
print(math.log10(100))  # Output: 2.0

print(math.sin(math.pi/2))  # Output: 1.0
print(math.cos(math.pi))  # Output: -1.0
print(math.tan(math.pi/4))  # Output: 1.0
print(math.degrees(math.pi/3))  # Output: 60.0  转为角度
print(math.radians(60))  # Output: 1.0471975511965976    转为弧度

#随机数
import random


print(random.random())  # Output: 0.17970987693706136   此代码用于生成并打印一个随机浮点数。
print(random.randint(1, 10))  # Output: 7   此代码用于生成一个1到10之间的随机整数，并将其打印到控制台。
print(random.choice([1, 2, 3, 4, 5]))  # Output: 4   此代码用于从列表中随机选择一个元素，并将其打印到控制台。
print(random.sample([1, 2, 3, 4, 5], 2))  # Output: [3, 5]   此代码用于从列表中随机选择两个元素，并将其打印到控制台。


i = range(10)
print(i) # Output:此代码用于打印从0到9的数字范围。