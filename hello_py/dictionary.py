# -*- coding: gbk -*-
# Author: style_forever
# Date: 10
# Description: 




# �б�������Ķ��󼯺ϣ��ֵ�������Ķ��󼯺ϡ�����֮����������ڣ��ֵ䵱�е�Ԫ����ͨ��������ȡ�ģ�������ͨ��ƫ�ƴ�ȡ��

# �ֵ���һ��ӳ�����ͣ��ֵ��� { } ��ʶ������һ������� ��(key) : ֵ(value) �ļ��ϡ�

# ��(key)����ʹ�ò��ɱ����͡�

# ��ͬһ���ֵ��У���(key)������Ψһ�ġ�

#!/usr/bin/python3

dict = {}
dict['one'] = "1 - ����̳�"
dict[2]     = "2 - ���񹤾�"

tiny_dict = {'name': 'python','code':1, 'site': 'www.python.com'}


print (dict['one'])       # �����Ϊ 'one' ��ֵ
print (dict[2])           # �����Ϊ 2 ��ֵ
print (tiny_dict)          # ����������ֵ�
print (tiny_dict.keys())   # ������м�
print (tiny_dict.values()) # �������ֵ

#dictionary �����ú���
d = {"name": "Alice", "age": 25}
print(d.get("name"))         # ���: Alice
print(d.get("gender", "N/A")) # ���: N/A
print(len(d))  # ���: 2

print(d.keys())              # ���: dict_keys(['name', 'age'])
print(d.values())    # ���: dict_values(['Alice', 25])
print(d.items())     # ���: dict_items([('name', 'Alice'), ('age', 25)])  ����һ�������ֵ����м�ֵ�Ե���ͼ����

print("name" in d)  # ���: True
print("gender" in d)  # ���: False

d.update({"age": 26, "gender": "female"})
print(d)  # ���: {'name': 'Alice', 'age': 26, 'gender': 'female'}

d.pop("age")
print(d)  # ���: {'name': 'Alice', 'gender': 'female'}

d_copy = d.copy()
print(d_copy)  # ���: {'name': 'Alice', 'age': 25}

keys = ["name", "age", "gender"]
new_dict = dict.fromkeys(keys, "unknown")
print(new_dict)  # ���: {'name': 'unknown', 'age': 'unknown', 'gender': 'unknown'}

d.clear()
print(d)  # ���: {}     ����ֵ�