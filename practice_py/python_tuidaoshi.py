# -*- coding: gbk -*-
# Author: style_forever
# Date: 11
# Description: 



# 常见的推导式示例：

# 1. 列表推导式
# 生成一个包含1到10的平方的列表
squares = [x**2 for x in range(1, 11)]
print(squares)

# 2. 字典推导式
# 生成一个包含1到10的偶数和奇数的字典
even_odd = {x: 'even' if x % 2 == 0 else 'odd' for x in range(1, 11)}
print(even_odd)

# 3. 集合推导式
# 生成一个包含1到10的偶数的集合
evens = {x for x in range(1, 11) if x % 2 == 0}
print(evens)

# 4. 条件推导式
# 生成一个包含1到10的偶数的列表
evens = [x for x in range(1, 11) if x % 2 == 0] 
print(evens)

numbers = range(1, 11)
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# 5. 嵌套推导式
# 生成一个包含1到10的平方的列表，每个元素是该元素的平方和它的平方根
squares_and_roots = [(x**2, x**0.5) for x in range(1, 11)]
print(squares_and_roots)