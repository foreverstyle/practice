# -*- coding: gbk -*-
# Author: style_forever
# Date: 12
# Description: 

# 在 Python 中，类（class）是用来创建对象的蓝图。类封装了数据（属性）和操作这些数据的方法（方法）。


class ClassName:      #class 关键字用于定义一个新类。ClassName 是类的名字，通常遵循 PascalCase（每个单词的首字母大写）。
    # 类的属性
    class_attribute = 'class attribute'

    def __init__(self, instance_attribute):     #左右两边各两个下划线
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

#self: 代表实例对象，用于访问该实例的属性和方法。
# 实例属性通常在类的构造函数 __init__ 中定义，并通过 self 进行初始化。这样，每个实例都可以有不同的属性值。
# 外部可以访问的属性 self不是关键字，可以用其他名字代替。

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

print(car1.make)  # 输出: Toyota    通过self.make直接访问实例属性
print(car1.model)  # 输出: Corolla   通过self.model直接访问实例属性

print(Car.wheels)  # 输出: 4         通过类名访问类属性

print(car1.description())  # 输出: Toyota Corolla with 4 wheels
print(car2.description())  # 输出: Honda Civic with 4 wheels

# 修改实例属性
car1.make = "Nissan"
print(car1.description())  # 输出: Nissan Corolla with 4 wheels

# 修改类属性
Car.wheels = 5
print(car1.description())  # 输出: Nissan Corolla with 5 wheels
print(car2.description())  # 输出: Honda Civic with 5 wheels


class Dog:
    species = "Canine"  # 类属性

    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age    # 实例属性

dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 7)

# 修改 dog1.species
dog1.species = "Dog"

print(dog1.species)  # 输出: Dog
print(dog2.species)  # 输出: Canine
print(Dog.species)   # 输出: Canine


#访问类属性: 当你通过 dog1.species 访问 species 时，Python 会首先在 dog1 的实例属性中查找 species，如果找不到，它才会去类属性中查找。

#修改类属性？: 当你通过 dog1.species = "Dog" 来“修改” species 时，实际上 dog1 并没有修改 Dog 类的 species 类属性，而是在 dog1 的实例上创建了一个名为 species 的实例属性


#dog1.species 会输出 "Dog"，因为 dog1 实例上有了自己的 species 实例属性。
# dog2.species 和 Dog.species 仍然会输出 "Canine"，因为 dog2 没有自己的 species 实例属性，它们依然在访问类属性。

# 如果你想真正修改类属性而不是创建实例属性，应该直接通过类来修改：




# 继承
# 继承是面向对象编程的一个重要概念。它允许创建新的类，从现有类继承属性和方法，并添加新的属性和方法。
# 继承的语法如下：

# class ParentClass:
#     def method1(self):
#         pass

#     def method2(self):
#         pass

# class ChildClass(ParentClass):
#     def method3(self):
#         pass


#!/usr/bin/python3
# 类属性与方法
# 类的私有属性
# __private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。

 
#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
 
 
 
s = student('style',20,60,3)
s.speak()

# 方法重写
# 子类中如果定义了与父类同名的方法，则子类的方法覆盖父类的方法。
# 子类中如果调用父类的方法，则总是调用子类的方法，不会调用父类的方法。
# 子类中如果需要调用父类的方法，可以通过 
    #1.类名.方法名
    #2.super().方法名

#!/usr/bin/python3
 
class Parent:        # 定义父类
   def myMethod(self):
      print ('调用父类方法')
 
class Child(Parent): # 定义子类
   def myMethod(self):
      print ('调用子类方法')
 
c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法
super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法


# 类的专有方法：
# __init__ : 构造函数，在生成对象时调用
# __del__ : 析构函数，释放对象时使用
# __repr__ : 打印，转换 当调用 repr() 或者在交互式解释器中直接输入对象名时自动调用
# __setitem__ : 按照索引赋值    使用索引赋值时自动调用。
# __getitem__: 按照索引获取值   使用索引访问值时自动调用

# __len__: 获得长度 使用 len() 时自动调用

# __cmp__: 比较运算 使用比较运算符时自动调用。已弃用，建议使用 __eq__ 和 __ne__ 。
# __eq__: 等于运算
# __ne__: 不等于运算
# __lt__: 小于运算
# __le__: 小于等于运算
# __gt__: 大于运算
# __ge__: 大于等于运算

# __call__: 函数调用


# __str__: 输出转换为字符串   使用 str() 时自动调用或者打印输出时调用。

# __add__: 加运算   加法运算时自动调用
# __sub__: 减运算    减法运算时自动调用
# __mul__: 乘运算    乘法运算时自动调用
# __truediv__: 除运算   除法运算时自动调用
# __mod__: 求余运算   求余运算时自动调用
# __pow__: 乘方   乘方运算时自动调用



# __del__ : 析构函数，释放对象时使用
class MyClass:
    def __del__(self):
        print("Object is being deleted")

obj = MyClass()  
del obj  # __del__ 被调用


# __add__: 加运算   加法运算时自动调用
class MyClass:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MyClass(self.value + other.value)

obj1 = MyClass(10)
obj2 = MyClass(20)
result = obj1 + obj2  # __add__ 被调用


# __str__: 输出转换为字符串
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
 
   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
 
v1 = Vector(2,10)       
v2 = Vector(5,-2)
print (v1 + v2)         # 调用 __str__ 方法，输出结果为：Vector (7, 8)



#多继承
# 一个类可以从多个父类继承方法和属性。

class A:
    def feature_a(self):
        print("Feature A")

class B:
    def feature_b(self):
        print("Feature B")

class C(A, B):
    def feature_c(self):
        print("Feature C")

# 实例化子类 C
c = C()
c.feature_a()  # 调用从 A 类继承的方法
c.feature_b()  # 调用从 B 类继承的方法
c.feature_c()  # 调用 C 类自身的方法


# 命名冲突问题：靠近原则
# 子类和父类中存在同名的方法或属性时，会造成命名冲突。
# Python 采用了“靠近原则”，即，在子类中查找方法或属性，如果没有找到，则继续在父类中查找。

class A:
    def greeting(self):
        print("Hello from A")

class B:
    def greeting(self):
        print("Hello from B")

class C(A, B):
    pass

c = C()
c.greeting()  # 输出: Hello from A

#覆写父类的方法


#多态
# 多态是指允许不同类的对象对同一消息作出不同的响应。在面向对象编程中，多态意味着一个方法或属性可以接收不同类的对象，并作出不同的响应。

# 1. 重写父类的方法
# 2. 子类实现父类接口

class Animal:
    def speak(self):        #抽象类 顶层设计，设计一个框架 代码pass
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):      
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):      #接口
    print(animal.speak())

dog = Dog()
cat = Cat()

make_animal_speak(dog)  # 输出: Woof!
make_animal_speak(cat)  # 输出: Meow!
