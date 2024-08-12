# -*- coding: gbk -*-
# Author: style_forever
# Date: 12
# Description: 

# 在 Python 中，类（class）是用来创建对象的蓝图。类封装了数据（属性）和操作这些数据的方法（方法）。


class ClassName:      #class 关键字用于定义一个新类。ClassName 是类的名字，通常遵循 PascalCase（每个单词的首字母大写）。
    # 类的属性
    class_attribute = 'class attribute'

    def __init__(self, instance_attribute):
        # 实例属性
        self.instance_attribute = instance_attribute

    def method(self):
        # 实例方法
        print('This is a method. Instance attribute:', self.instance_attribute)

    @classmethod
    def class_method(cls):
        # 类方法
        print('This is a class method. Class attribute:', cls.class_attribute)

    @staticmethod
    def static_method():
        # 静态方法
        print('This is a static method.')

# 创建实例
obj = ClassName('instance attribute')

# 访问和调用
print(obj.instance_attribute)  # 输出: instance attribute
obj.method()  # 输出: This is a method. Instance attribute: instance attribute

# 访问类属性和方法
print(ClassName.class_attribute)  # 输出: class attribute
ClassName.class_method()  # 输出: This is a class method. Class attribute: class attribute

# 调用静态方法
ClassName.static_method()  # 输出: This is a static method.



class Person:
    def __init__(self, name, age):          #外部可以访问的属性 类内函数括号内带self均表示实例属性
        self.name = name  # 实例属性
        self.age = age    # 实例属性

person1 = Person("Alice", 30)
print(person1.name)  # 输出: Alice
print(person1.age)   # 输出: 30

person1.name = "Bob"  # 修改实例属性
print(person1.name)  # 输出: Bob


# 实例属性 vs. 类属性
# 实例属性: 绑定到实例对象，每个实例都有自己的副本。通过 self 访问。例如：self.name、self.age。
# 类属性: 绑定到类本身，所有实例共享一个副本。通过类名访问。例如：Person.species = "Homo sapiens"。
# make 和 model 是实例属性，它们是特定于每个 Car 实例的。
# wheels 是类属性，所有 Car 实例共享一个值。

class Car:
    # 类属性
    wheels = 4

    def __init__(self, make, model):
        # 实例属性
        self.make = make
        self.model = model

    def description(self):
        return f"{self.make} {self.model} with {Car.wheels} wheels"

# 创建实例
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.description())  # 输出: Toyota Corolla with 4 wheels
print(car2.description())  # 输出: Honda Civic with 4 wheels

# 修改实例属性
car1.make = "Nissan"
print(car1.description())  # 输出: Nissan Corolla with 4 wheels

# 修改类属性
Car.wheels = 5
print(car1.description())  # 输出: Nissan Corolla with 5 wheels
print(car2.description())  # 输出: Honda Civic with 5 wheels
