# -*- coding: gbk -*-
# Author: style_forever
# Date: 12
# Description: 

# �� Python �У��ࣨclass�������������������ͼ�����װ�����ݣ����ԣ��Ͳ�����Щ���ݵķ�������������


class ClassName:      #class �ؼ������ڶ���һ�����ࡣClassName ��������֣�ͨ����ѭ PascalCase��ÿ�����ʵ�����ĸ��д����
    # �������
    class_attribute = 'class attribute'

    def __init__(self, instance_attribute):     #�������߸������»���
        # ʵ������
        self.instance_attribute = instance_attribute

    def method(self):
        # ʵ������
        print('This is a method. Instance attribute:', self.instance_attribute)

    @classmethod
    def class_method(cls):
        # �෽��
        print('This is a class method. Class attribute:', cls.class_attribute)

    @staticmethod
    def static_method():
        # ��̬����
        print('This is a static method.')

# ����ʵ��
obj = ClassName('instance attribute')

# ���ʺ͵���
print(obj.instance_attribute)  # ���: instance attribute
obj.method()  # ���: This is a method. Instance attribute: instance attribute

# ���������Ժͷ���
print(ClassName.class_attribute)  # ���: class attribute
ClassName.class_method()  # ���: This is a class method. Class attribute: class attribute

# ���þ�̬����
ClassName.static_method()  # ���: This is a static method.

#self: ����ʵ���������ڷ��ʸ�ʵ�������Ժͷ�����
# ʵ������ͨ������Ĺ��캯�� __init__ �ж��壬��ͨ�� self ���г�ʼ����������ÿ��ʵ���������в�ͬ������ֵ��
# �ⲿ���Է��ʵ����� self���ǹؼ��֣��������������ִ��档

class Person:
    def __init__(self, name, age):          #�ⲿ���Է��ʵ����� ���ں��������ڴ�self����ʾʵ������
        self.name = name  # ʵ������
        self.age = age    # ʵ������

person1 = Person("Alice", 30)
print(person1.name)  # ���: Alice
print(person1.age)   # ���: 30

person1.name = "Bob"  # �޸�ʵ������
print(person1.name)  # ���: Bob


# ʵ������ vs. ������
# ʵ������: �󶨵�ʵ������ÿ��ʵ�������Լ��ĸ�����ͨ�� self ���ʡ����磺self.name��self.age��
# ������: �󶨵��౾������ʵ������һ��������ͨ���������ʡ����磺Person.species = "Homo sapiens"��
# make �� model ��ʵ�����ԣ��������ض���ÿ�� Car ʵ���ġ�
# wheels �������ԣ����� Car ʵ������һ��ֵ��

class Car:
    # ������
    wheels = 4

    def __init__(self, make, model):
        # ʵ������
        self.make = make
        self.model = model

    def description(self):
        return f"{self.make} {self.model} with {Car.wheels} wheels"

# ����ʵ��
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.make)  # ���: Toyota    ͨ��self.makeֱ�ӷ���ʵ������
print(car1.model)  # ���: Corolla   ͨ��self.modelֱ�ӷ���ʵ������

print(Car.wheels)  # ���: 4         ͨ����������������

print(car1.description())  # ���: Toyota Corolla with 4 wheels
print(car2.description())  # ���: Honda Civic with 4 wheels

# �޸�ʵ������
car1.make = "Nissan"
print(car1.description())  # ���: Nissan Corolla with 4 wheels

# �޸�������
Car.wheels = 5
print(car1.description())  # ���: Nissan Corolla with 5 wheels
print(car2.description())  # ���: Honda Civic with 5 wheels


class Dog:
    species = "Canine"  # ������

    def __init__(self, name, age):
        self.name = name  # ʵ������
        self.age = age    # ʵ������

dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 7)

# �޸� dog1.species
dog1.species = "Dog"

print(dog1.species)  # ���: Dog
print(dog2.species)  # ���: Canine
print(Dog.species)   # ���: Canine


#����������: ����ͨ�� dog1.species ���� species ʱ��Python �������� dog1 ��ʵ�������в��� species������Ҳ��������Ż�ȥ�������в��ҡ�

#�޸������ԣ�: ����ͨ�� dog1.species = "Dog" �����޸ġ� species ʱ��ʵ���� dog1 ��û���޸� Dog ��� species �����ԣ������� dog1 ��ʵ���ϴ�����һ����Ϊ species ��ʵ������


#dog1.species ����� "Dog"����Ϊ dog1 ʵ���������Լ��� species ʵ�����ԡ�
# dog2.species �� Dog.species ��Ȼ����� "Canine"����Ϊ dog2 û���Լ��� species ʵ�����ԣ�������Ȼ�ڷ��������ԡ�

# ������������޸������Զ����Ǵ���ʵ�����ԣ�Ӧ��ֱ��ͨ�������޸ģ�




# �̳�
# �̳�����������̵�һ����Ҫ������������µ��࣬��������̳����Ժͷ�����������µ����Ժͷ�����
# �̳е��﷨���£�

# class ParentClass:
#     def method1(self):
#         pass

#     def method2(self):
#         pass

# class ChildClass(ParentClass):
#     def method3(self):
#         pass


#!/usr/bin/python3
# �������뷽��
# ���˽������
# __private_attrs�������»��߿�ͷ������������Ϊ˽�У�����������ⲿ��ʹ�û�ֱ�ӷ��ʡ������ڲ��ķ�����ʹ��ʱ self.__private_attrs��

 
#�ඨ��
class people:
    #�����������
    name = ''
    age = 0
    #����˽������,˽�����������ⲿ�޷�ֱ�ӽ��з���
    __weight = 0
    #���幹�췽��
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s ˵: �� %d �ꡣ" %(self.name,self.age))
 
#���̳�ʾ��
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #���ø���Ĺ���
        people.__init__(self,n,a,w)
        self.grade = g
    #��д����ķ���
    def speak(self):
        print("%s ˵: �� %d ���ˣ����ڶ� %d �꼶"%(self.name,self.age,self.grade))
 
 
 
s = student('style',20,60,3)
s.speak()

# ������д
# ����������������븸��ͬ���ķ�����������ķ������Ǹ���ķ�����
# ������������ø���ķ����������ǵ�������ķ�����������ø���ķ�����
# �����������Ҫ���ø���ķ���������ͨ�� 
    #1.����.������
    #2.super().������

#!/usr/bin/python3
 
class Parent:        # ���常��
   def myMethod(self):
      print ('���ø��෽��')
 
class Child(Parent): # ��������
   def myMethod(self):
      print ('�������෽��')
 
c = Child()          # ����ʵ��
c.myMethod()         # ���������д����
super(Child,c).myMethod() #�����������ø����ѱ����ǵķ���


# ���ר�з�����
# __init__ : ���캯���������ɶ���ʱ����
# __del__ : �����������ͷŶ���ʱʹ��
# __repr__ : ��ӡ��ת�� ������ repr() �����ڽ���ʽ��������ֱ�����������ʱ�Զ�����
# __setitem__ : ����������ֵ    ʹ��������ֵʱ�Զ����á�
# __getitem__: ����������ȡֵ   ʹ����������ֵʱ�Զ�����

# __len__: ��ó��� ʹ�� len() ʱ�Զ�����

# __cmp__: �Ƚ����� ʹ�ñȽ������ʱ�Զ����á������ã�����ʹ�� __eq__ �� __ne__ ��
# __eq__: ��������
# __ne__: ����������
# __lt__: С������
# __le__: С�ڵ�������
# __gt__: ��������
# __ge__: ���ڵ�������

# __call__: ��������


# __str__: ���ת��Ϊ�ַ���   ʹ�� str() ʱ�Զ����û��ߴ�ӡ���ʱ���á�

# __add__: ������   �ӷ�����ʱ�Զ�����
# __sub__: ������    ��������ʱ�Զ�����
# __mul__: ������    �˷�����ʱ�Զ�����
# __truediv__: ������   ��������ʱ�Զ�����
# __mod__: ��������   ��������ʱ�Զ�����
# __pow__: �˷�   �˷�����ʱ�Զ�����



# __del__ : �����������ͷŶ���ʱʹ��
class MyClass:
    def __del__(self):
        print("Object is being deleted")

obj = MyClass()  
del obj  # __del__ ������


# __add__: ������   �ӷ�����ʱ�Զ�����
class MyClass:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MyClass(self.value + other.value)

obj1 = MyClass(10)
obj2 = MyClass(20)
result = obj1 + obj2  # __add__ ������


# __str__: ���ת��Ϊ�ַ���
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
print (v1 + v2)         # ���� __str__ ������������Ϊ��Vector (7, 8)



#��̳�
# һ������ԴӶ������̳з��������ԡ�

class A:
    def feature_a(self):
        print("Feature A")

class B:
    def feature_b(self):
        print("Feature B")

class C(A, B):
    def feature_c(self):
        print("Feature C")

# ʵ�������� C
c = C()
c.feature_a()  # ���ô� A ��̳еķ���
c.feature_b()  # ���ô� B ��̳еķ���
c.feature_c()  # ���� C ������ķ���


# ������ͻ���⣺����ԭ��
# ����͸����д���ͬ���ķ���������ʱ�������������ͻ��
# Python �����ˡ�����ԭ�򡱣������������в��ҷ��������ԣ����û���ҵ���������ڸ����в��ҡ�

class A:
    def greeting(self):
        print("Hello from A")

class B:
    def greeting(self):
        print("Hello from B")

class C(A, B):
    pass

c = C()
c.greeting()  # ���: Hello from A

#��д����ķ���


#��̬
# ��̬��ָ����ͬ��Ķ����ͬһ��Ϣ������ͬ����Ӧ��������������У���̬��ζ��һ�����������Կ��Խ��ղ�ͬ��Ķ��󣬲�������ͬ����Ӧ��

# 1. ��д����ķ���
# 2. ����ʵ�ָ���ӿ�

class Animal:
    def speak(self):        #������ ������ƣ����һ����� ����pass
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):      
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):      #�ӿ�
    print(animal.speak())

dog = Dog()
cat = Cat()

make_animal_speak(dog)  # ���: Woof!
make_animal_speak(cat)  # ���: Meow!
