# -*- coding: gbk -*-
# Author: style_forever
# Date: 12
# Description: 

# �� Python �У��ࣨclass�������������������ͼ�����װ�����ݣ����ԣ��Ͳ�����Щ���ݵķ�������������


class ClassName:      #class �ؼ������ڶ���һ�����ࡣClassName ��������֣�ͨ����ѭ PascalCase��ÿ�����ʵ�����ĸ��д����
    # �������
    class_attribute = 'class attribute'

    def __init__(self, instance_attribute):
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

print(car1.description())  # ���: Toyota Corolla with 4 wheels
print(car2.description())  # ���: Honda Civic with 4 wheels

# �޸�ʵ������
car1.make = "Nissan"
print(car1.description())  # ���: Nissan Corolla with 4 wheels

# �޸�������
Car.wheels = 5
print(car1.description())  # ���: Nissan Corolla with 5 wheels
print(car2.description())  # ���: Honda Civic with 5 wheels
