# -*- coding: gbk -*-
# Author: style_forever
# Date: 09
# Description: 

#!/usr/bin/python3

tuple1 = ( 'abcd', 786 , 2.23, 'python', 70.2  )
tiny_tuple = (123, 'python')

print (tuple1)             # �������Ԫ��
print (tuple1[0])          # ���Ԫ��ĵ�һ��Ԫ��
print (tuple1[1:3])        # ����ӵڶ���Ԫ�ؿ�ʼ��������Ԫ��
print (tuple1[2:])         # ����ӵ�����Ԫ�ؿ�ʼ������Ԫ��
print (tiny_tuple * 2)     # �������Ԫ��
print (tuple1 + tiny_tuple) # ����Ԫ��

# ���԰��ַ�������һ�������Ԫ�顣�ַ�����ÿ���ַ�����Ԫ���һ��Ԫ�ء���ˣ��ַ���Ҳ���Ա���������Ƭ��

# ��Ȼtuple��Ԫ�ز��ɸı䣬�������԰����ɱ�Ķ��󣬱���list�б����ַ���һ����Ԫ���Ԫ�ز����޸ġ�

# ������Ԫ�飺
empty_tuple = tuple()
print(empty_tuple)  # Output: ()

# # ���б���Ԫ�飺
tuple_from_list = tuple([1, 2, 3])
print(tuple_from_list)  # Output: (1, 2, 3)

# # ���ַ�������Ԫ�飺
tuple_from_str = tuple("hello")
print(tuple_from_str)  # Output: ('h', 'e', 'l', 'l', 'o')

