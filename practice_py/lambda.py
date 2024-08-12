# -*- coding: gbk -*-
# Author: style_forever
# Date: 12
# Description: 

# Python ʹ�� lambda ����������������

# ��ν�������⼴����ʹ�� def ���������׼����ʽ����һ��������

# lambda ֻ��һ�����ʽ��������� def �򵥺ܶࡣ
# lambda ��������һ�����ʽ��������һ������顣�������� lambda ���ʽ�з�װ���޵��߼���ȥ��
# lambda [arg1 [,arg2,.....arg]]:expression

# 1. �в�������������
# ����һ����������֮�͵�����������

sum = lambda a, b: a + b
print(sum(1, 2))  # ��� 3

# 2. �޲�������������
# ����һ����� "hello world" ������������


hello = lambda: print("hello world")
hello()  # ��� hello world

# 3. ����������Ϊ����
# ����һ�����б�������Ԫ�ص�ƽ��������������

square = lambda x: x ** 2
print(list(map(square, [1, 2, 3, 4, 5])))  # ��� [1, 4, 9, 16, 25]

# 4. ����������Ϊ����ֵ
# ����һ����������֮�̵�����������

division = lambda a, b: a / b
print(division(10, 3))  # ��� 3.3333333333333335


# lambda ����ͨ�������ú����� map()��filter() �� reduce() һ��ʹ�ã��Ա��ڼ�����ִ�в��������磺

# 5. ����������Ϊ���ú����Ĳ���
# ����һ�����б�������Ԫ�ص�ƽ������������������Ϊ map() �����Ĳ�����

squares = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
print(squares)  # ��� [1, 4, 9, 16, 25]