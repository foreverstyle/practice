# -*- coding: gbk -*-
# Author: style_forever
# Date: 10
# Description: 

# Python �еļ��ϣ�Set����һ�����򡢿ɱ���������ͣ����ڴ洢Ψһ��Ԫ�ء�

# �����е�Ԫ�ز����ظ������ҿ��Խ��н�������������ȳ����ļ��ϲ�����

# �� Python �У�����ʹ�ô����� {} ��ʾ��Ԫ��֮���ö��� , �ָ���

# ���⣬Ҳ����ʹ�� set() �����������ϡ�

# ע�⣺����һ���ռ��ϱ����� set() ������ { }����Ϊ { } ����������һ�����ֵ䡣

# ������ʽ��

#!/usr/bin/python3

sites = {'Google', 'Run_oob', 'Facebook', 'Baidu'}

print(sites)   # ������ϣ��ظ���Ԫ�ر��Զ�ȥ��

# ��Ա����
if 'Run_oob' in sites :
    print('Run_oob �ڼ�����')
else :
    print('Run_oob ���ڼ�����')


# set���Խ��м�������
a = set('abracadabra')
b = set('abc')

print(a)

print(a - b)     # a �� b �Ĳ

print(a | b)     # a �� b �Ĳ���

print(a & b)     # a �� b �Ľ���

print(a ^ b)     # a �� b �в�ͬʱ���ڵ�Ԫ��

# ���ϵ����ú���

print(len(sites))  # ���ϵ�Ԫ�ظ���

print(sites.add('Tao_bao'))  # �򼯺������Ԫ��

print(sites)

print(sites.remove('Tao_bao'))  # �Ӽ�����ɾ��Ԫ��

print(sites)

print(sites.pop())  # ���ɾ�������е�һ��Ԫ��

print(sites)

print(sites.clear())  # ��ռ���

print(sites)


# �����ռ���
empty_set = set()
print(empty_set)  # Output: set()

# ���б�������ɵ������󴴽����ϣ�
set_from_list = set([1, 2, 2, 3, 4])
print(set_from_list)  # Output: {1, 2, 3, 4}  (�ظ���Ԫ�ر��Զ�ȥ��)

# ���ַ����������ϣ�
set_from_str = set("hello")
print(set_from_str)  # Output: {'h', 'e', 'l', 'o'}

