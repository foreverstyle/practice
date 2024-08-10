# -*- coding: gbk -*-
# Author: style_forever
# Date: 10
# Description: 




# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。

# 键(key)必须使用不可变类型。

# 在同一个字典中，键(key)必须是唯一的。

#!/usr/bin/python3

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tiny_dict = {'name': 'python','code':1, 'site': 'www.python.com'}


print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tiny_dict)          # 输出完整的字典
print (tiny_dict.keys())   # 输出所有键
print (tiny_dict.values()) # 输出所有值

#dictionary 的内置函数
d = {"name": "Alice", "age": 25}
print(d.get("name"))         # 输出: Alice
print(d.get("gender", "N/A")) # 输出: N/A
print(len(d))  # 输出: 2

print(d.keys())              # 输出: dict_keys(['name', 'age'])
print(d.values())    # 输出: dict_values(['Alice', 25])
print(d.items())     # 输出: dict_items([('name', 'Alice'), ('age', 25)])  返回一个包含字典所有键值对的视图对象

print("name" in d)  # 输出: True
print("gender" in d)  # 输出: False

d.update({"age": 26, "gender": "female"})
print(d)  # 输出: {'name': 'Alice', 'age': 26, 'gender': 'female'}

d.pop("age")
print(d)  # 输出: {'name': 'Alice', 'gender': 'female'}

d_copy = d.copy()
print(d_copy)  # 输出: {'name': 'Alice', 'age': 25}

keys = ["name", "age", "gender"]
new_dict = dict.fromkeys(keys, "unknown")
print(new_dict)  # 输出: {'name': 'unknown', 'age': 'unknown', 'gender': 'unknown'}

d.clear()
print(d)  # 输出: {}     清空字典