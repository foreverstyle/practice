# -*- coding: gbk -*-
# Python������ͬʱΪ���������ֵ�����磺

a = b = c = 1
print(a,b,c) # Output: 1 1 1

a, b, c = 1, 2, "python"
print(a, b, c) # Output: 1 2 python

a, b, c = 5, 6, 7
print(a / b)
print(a // b)
print(a % b)
print(a ** b)



#��ѧ����
import math

print(math.sqrt(16))  # Output: 4.0
print(math.pow(2, 3))  # Output: 8.0

print(math.floor(3.7))  # Output: 3 ��ȡ��
print(math.ceil(3.2))  # Output: 4 ��ȡ��
print(round(3.2))  # Output: 3 ��������

print(math.exp(2))  # Output: 7.38905609893065

print(math.log(10))  # Output: 2.302585092994046  Ĭ����eΪ��
print(math.log(10, 10))  # Output: 1.0 �ڶ��������ǵ���
print(math.log10(100))  # Output: 2.0

print(math.sin(math.pi/2))  # Output: 1.0
print(math.cos(math.pi))  # Output: -1.0
print(math.tan(math.pi/4))  # Output: 1.0
print(math.degrees(math.pi/3))  # Output: 60.0  תΪ�Ƕ�
print(math.radians(60))  # Output: 1.0471975511965976    תΪ����

#�����
import random


print(random.random())  # Output: 0.17970987693706136   �˴����������ɲ���ӡһ�������������
print(random.randint(1, 10))  # Output: 7   �˴�����������һ��1��10֮�������������������ӡ������̨��
print(random.choice([1, 2, 3, 4, 5]))  # Output: 4   �˴������ڴ��б������ѡ��һ��Ԫ�أ��������ӡ������̨��
print(random.sample([1, 2, 3, 4, 5], 2))  # Output: [3, 5]   �˴������ڴ��б������ѡ������Ԫ�أ��������ӡ������̨��


i = range(10)
print(i) # Output:�˴������ڴ�ӡ��0��9�����ַ�Χ��