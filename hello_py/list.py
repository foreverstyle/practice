# -*- coding: gbk -*-

# List���б� �� Python ��ʹ����Ƶ�����������͡�

# �б������ɴ��������������ݽṹʵ�֡��б���Ԫ�ص����Ϳ��Բ���ͬ����֧�����֣��ַ����������԰����б���νǶ�ף���

# �б���д�ڷ����� [] ֮�䡢�ö��ŷָ�����Ԫ���б�

# ���ַ���һ�����б�ͬ�����Ա������ͽ�ȡ���б���ȡ�󷵻�һ����������Ԫ�ص����б�

# �б��ȡ���﷨��ʽ���£�

#!/usr/bin/python3

list1 = [ 'abcd', 786 , 2.23, 'python', 70.2 ]  # ����һ���б�
list2 = [123, 'python']

print (list1)            # ��ӡ�����б�
print (list1[0])         # ��ӡ�б�ĵ�һ��Ԫ��
print (list1[1:3])       # ��ӡ�б�ڶ������ĸ�Ԫ�أ����������ĸ�Ԫ�أ�
print (list1[2:])        # ��ӡ�б�ӵ�����Ԫ�ؿ�ʼ��ĩβ
print (list2 * 2)    # ��ӡlist2�б�����
print (list1 + list2)  # ��ӡ�����б�ƴ����һ��Ľ��

# ��Python�ַ�����һ�����ǣ��б��е�Ԫ���ǿ��Ըı��
# ��һ����ͷ���ڶ�����β���������ǲ������������Ϊ���������ʾ����

#list�����ú���
lst = [1, 2, 3]
print(lst.count(2))  # ���: 1
print(lst.index(2))  # ���: 1

print(len(lst)) # ���: 3

print(2 in lst)  # ���: True
print(4 in lst)  # ���: False

print(min(lst))  # ���: 1
print(max(lst))  # ���: 3
print(sum(lst))  # ���: 6


lst.append(4)
print(lst)  # ���: [1, 2, 3, 4]

lst.extend([4, 5])
print(lst) #    ���: [1, 2, 3, 4, 4, 5]

lst.insert(1, "a")
print(lst)  # ���: [1, 'a', 2, 3, 4, 4, 5]

lst.remove(2)
print(lst)  # ���: [1, 'a', 3, 4, 4, 5]    �Ƴ���һ��2

lst.pop()
print(lst)  # ���: [1, 'a', 3, 4, 4]   ɾ�����һ��Ԫ��

lst.pop(1)
print(lst)  # ���: [1, 3, 4, 4]    ɾ���ڶ���Ԫ��

lst.reverse()
print(lst)  # ���: [4, 4, 3, 'a', 1]

lst.sort()
print(lst)  # ���: [1, 3, 4, 4, 'a']  



# ���� operator ģ��
import operator

a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a,b))
print("operator.eq(c,b): ", operator.eq(c,b))

# list() �����ڴ����б�����ú����������Խ��ɵ����������ַ�����Ԫ�顢�ֵ�ȣ�ת��Ϊ�б����ߴ���һ�����б�

# �﷨��ʽ���£�
# �������б�
empty_list = list()
print(empty_list)  # Output: []

# ���ַ���ת��Ϊ�б�
str_list = list("hello")
print(str_list)  # Output: ['h', 'e', 'l', 'l', 'o']

# ��Ԫ��ת��Ϊ�б�
tuple_list = list((1, 2, 3))
print(tuple_list)  # Output: [1, 2, 3]

