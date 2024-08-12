# -*- coding: gbk -*-
# Author: style_forever
# Date: 11
# Description: 


# �ɵ�������Iterable��
# ���壺һ���ɵ���������һ�����Է���һ���������Ķ�������ζ�������Ա� for ѭ������������˵�����ǿ������������Ԫ�ص����ݽṹ���ǿɵ����ġ�
# �����Ŀɵ�������
# �������ͣ����б� (list)��Ԫ�� (tuple)���ַ��� (str)���ֵ� (dict)������ (set)
# ��������generator�����������ص������Ķ���


# ��������Iterator��
# ���壺��������һ��ʵ���˵�����Э��Ķ�������������������__iter__() �� __next__()������˵����������һ���ڱ�����������һ����Ԫ�صĶ���
# ������������ģ�lazy evaluation����ֻ������Ҫʱ������Ԫ�ء�
# ������һ��������Ͳ����ٴα������������´�����

# ��������һ�����Լ�ס������λ�õĶ���
# ����������Ӽ��ϵĵ�һ��Ԫ�ؿ�ʼ���ʣ�ֱ�����е�Ԫ�ر������������������ֻ����ǰ������ˡ�

# ����������������������iter() �� next()��
# iter() ��������һ������������next() �����򷵻���һ��Ԫ�ء�
# 
# ���ǿ���ʹ�� iter() ������ȡһ������������Ȼ��ʹ�� next() �������ϻ�ȡ��һ��Ԫ�ء�
# 
# ���磬���ǿ���ʹ�� range() ��������һ����������


r = range(5)
print(r)  # range(0, 5)

it = iter(r)
print(it)  # <range_iterator object at 0x000001>

print(next(it))  # 0
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # 4

# ���ڵ�����ֻ����ǰ������ˣ����������޷�ʹ�� prev() ������ȡ��һ��Ԫ�ء�
# 
# ���ǣ����������Ա����³�ʼ����������ǿ��Զ�α���ͬһ�����У�



#!/usr/bin/python3
 
list=[1,2,3,4]
it = iter(list)    # ��������������
for x in it:
    print (x)



#������
class CountToN:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

# ʹ�õ�����
counter = CountToN(5)

for number in counter:
    print(number)




#������
def countdown(n):
    while n > 0:
        yield n     #�൱�ڵ�����return�����ǲ����������������Ƿ���һ������������
        n -= 1
 
# ��������������
generator = countdown(5)  #����iter���� 
 
# ͨ��������������ȡֵ
print(next(generator))  # ���: 5
print(next(generator))  # ���: 4
print(next(generator))  # ���: 3
 
# ʹ�� for ѭ������������
for value in generator:
    print(value)  # ���: 2 1



# �� Python �У�map()��filter() �� reduce() �����ڴ���ɵ�����������ú�����
# map() ������һ������Ӧ�õ�һ�������ɵ����������б�Ԫ��ȣ���ÿһ��Ԫ�أ�������һ��������������ͨ�� list() ת��Ϊ�б���
# filter() �������ڴӿɵ��������й��˳�����������Ԫ�أ�������һ����������  
# reduce() �������ڶԿɵ�����������ۻ�������������һ����һֵ��

# ���磬���ǿ���ʹ�� map() ���������б���ÿ��Ԫ�ص�ƽ����

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # [1, 4, 9, 16, 25]


# ���ǿ���ʹ�� filter() �������˵��б��е�ż����

numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]


# ���ǿ���ʹ�� reduce() ���������б���Ԫ�صĳ˻���

from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120