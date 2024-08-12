# -*- coding: gbk -*-
# Author: style_forever
# Date: 12
# Description: 



# 在 Python 中，可以使用列表（list）来实现栈的功能。栈是一种后进先出（LIFO, Last-In-First-Out）数据结构，意味着最后添加的元素最先被移除。特别是 append() 和 pop() 方法。

# 栈操作
# 压入（Push）: 将一个元素添加到栈的顶端。
# 弹出（Pop）: 移除并返回栈顶元素。
# 查看栈顶元素（Peek/Top）: 返回栈顶元素而不移除它。
# 检查是否为空（IsEmpty）: 检查栈是否为空。
# 获取栈的大小（Size）: 获取栈中元素的数量。

# 创建一个空栈
stack = []


# 向栈中添加元素
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  # 输出: [1, 2, 3]

# 弹出栈顶元素
top_element = stack.pop()
print(top_element)  # 输出: 3
print(stack)        # 输出: [1, 2]

# 查看栈顶元素（Peek/Top）
top_element = stack[-1]
print(top_element)  # 输出: 2

# 检查是否为空
is_empty = len(stack) == 0
print(is_empty)  # 输出: False

# 获取栈的大小
size = len(stack)  
print(size)       # 输出: 2

# self: 代表实例对象，用于访问该实例的属性和方法。
# self.stack: 表示实例的 stack 属性，存储在对象的内存中。通过 self 访问的属性可以在类的不同方法中共享和操作。
# 实例属性通常在类的构造函数 __init__ 中定义，并通过 self 进行初始化。这样，每个实例都可以有不同的属性值。
# 外部可以访问的属性

# class Person:
#     def __init__(self, name, age):
#         self.name = name  # 实例属性
#         self.age = age    # 实例属性

# person1 = Person("Alice", 30)
# print(person1.name)  # 输出: Alice
# print(person1.age)   # 输出: 30

# person1.name = "Bob"  # 修改实例属性
# print(person1.name)  # 输出: Bob



class Stack:
    def __init__(self):
        self.stack = [] #self.stack: 看成整体，相当于属于class的数据成员，可以改为其他名字，但最好不要与其他实例属性重名

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# 使用示例
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("栈顶元素:", stack.peek())  # 输出: 栈顶元素: 3
print("栈大小:", stack.size())    # 输出: 栈大小: 3

print("弹出元素:", stack.pop())  # 输出: 弹出元素: 3
print("栈是否为空:", stack.is_empty())  # 输出: 栈是否为空: False
print("栈大小:", stack.size())    # 输出: 栈大小: 2