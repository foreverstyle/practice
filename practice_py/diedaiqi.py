# -*- coding: gbk -*-
# Author: style_forever
# Date: 11
# Description: 


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