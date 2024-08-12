# -*- coding: gbk -*-
# Author: style_forever
# Date: 12
# Description: 



# �� Python �У�����ʹ���б�list����ʵ��ջ�Ĺ��ܡ�ջ��һ�ֺ���ȳ���LIFO, Last-In-First-Out�����ݽṹ����ζ�������ӵ�Ԫ�����ȱ��Ƴ����ر��� append() �� pop() ������

# ջ����
# ѹ�루Push��: ��һ��Ԫ����ӵ�ջ�Ķ��ˡ�
# ������Pop��: �Ƴ�������ջ��Ԫ�ء�
# �鿴ջ��Ԫ�أ�Peek/Top��: ����ջ��Ԫ�ض����Ƴ�����
# ����Ƿ�Ϊ�գ�IsEmpty��: ���ջ�Ƿ�Ϊ�ա�
# ��ȡջ�Ĵ�С��Size��: ��ȡջ��Ԫ�ص�������

# ����һ����ջ
stack = []


# ��ջ�����Ԫ��
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  # ���: [1, 2, 3]

# ����ջ��Ԫ��
top_element = stack.pop()
print(top_element)  # ���: 3
print(stack)        # ���: [1, 2]

# �鿴ջ��Ԫ�أ�Peek/Top��
top_element = stack[-1]
print(top_element)  # ���: 2

# ����Ƿ�Ϊ��
is_empty = len(stack) == 0
print(is_empty)  # ���: False

# ��ȡջ�Ĵ�С
size = len(stack)  
print(size)       # ���: 2

# self: ����ʵ���������ڷ��ʸ�ʵ�������Ժͷ�����
# self.stack: ��ʾʵ���� stack ���ԣ��洢�ڶ�����ڴ��С�ͨ�� self ���ʵ����Կ�������Ĳ�ͬ�����й���Ͳ�����
# ʵ������ͨ������Ĺ��캯�� __init__ �ж��壬��ͨ�� self ���г�ʼ����������ÿ��ʵ���������в�ͬ������ֵ��
# �ⲿ���Է��ʵ�����

# class Person:
#     def __init__(self, name, age):
#         self.name = name  # ʵ������
#         self.age = age    # ʵ������

# person1 = Person("Alice", 30)
# print(person1.name)  # ���: Alice
# print(person1.age)   # ���: 30

# person1.name = "Bob"  # �޸�ʵ������
# print(person1.name)  # ���: Bob



class Stack:
    def __init__(self):
        self.stack = [] #self.stack: �������壬�൱������class�����ݳ�Ա�����Ը�Ϊ�������֣�����ò�Ҫ������ʵ����������

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

# ʹ��ʾ��
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("ջ��Ԫ��:", stack.peek())  # ���: ջ��Ԫ��: 3
print("ջ��С:", stack.size())    # ���: ջ��С: 3

print("����Ԫ��:", stack.pop())  # ���: ����Ԫ��: 3
print("ջ�Ƿ�Ϊ��:", stack.is_empty())  # ���: ջ�Ƿ�Ϊ��: False
print("ջ��С:", stack.size())    # ���: ջ��С: 2