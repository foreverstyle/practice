# -*- coding: gbk -*-
# Author: style_forever
# Date: 12
# Description: 

# �ɸ���(mutable)�벻�ɸ���(immutable)����
# �� python �У�strings, tuples, �� numbers �ǲ��ɸ��ĵĶ��󣬶� list,dict �����ǿ����޸ĵĶ���

# ���ɱ����ͣ�������ֵ a=5 ���ٸ�ֵ a=10������ʵ����������һ�� int ֵ���� 10������ a ָ�������� 5 �����������Ǹı� a ��ֵ���൱���������� a��

# �ɱ����ͣ�������ֵ la=[1,2,3,4] ���ٸ�ֵ la[2]=5 ���ǽ� list la �ĵ�����Ԫ��ֵ���ģ�����laû�ж���ֻ�����ڲ���һ����ֵ���޸��ˡ�


# python �����Ĳ������ݣ�

# ���ɱ����ͣ����� C++ ��ֵ���ݣ����������ַ�����Ԫ�顣�� fun(a)�����ݵ�ֻ�� a ��ֵ��û��Ӱ�� a ����������� fun(a) �ڲ��޸� a ��ֵ������������һ�� a �Ķ���

# �ɱ����ͣ����� C++ �����ô��ݣ��� �б��ֵ䡣�� fun(la)�����ǽ� la �����Ĵ���ȥ���޸ĺ� fun �ⲿ�� la Ҳ����Ӱ��

def change(a):
    print(id(a))   # ָ�����ͬһ������
    a=10
    print(id(a))   # һ���¶���
 
a=1
print(id(a))
change(a)

#!/usr/bin/python3
 
# ��д����˵��
def change_me( my_list ):
   "�޸Ĵ�����б�"
   my_list.extend([1,2,3,4])
   print ("������ȡֵ: ", my_list)
   return
 
# ����change_me����
my_list = [10,20,30]
change_me( my_list )
print ("������ȡֵ: ", my_list)

# �����Ǻ� * �Ĳ�������Ԫ��(tuple)����ʽ���룬�������δ�����ı���������
# ���������Ǻ� ** �Ĳ��������ֵ����ʽ����
# ����ں�������ʱû��ָ��������������һ����Ԫ�顣����Ҳ���Բ���������δ�����ı���������ʵ����

#!/usr/bin/python3
 
# ��д����˵��
def print_info( arg1, *var_tuple ):
   "��ӡ�κδ���Ĳ���"
   print ("���: ")
   print (arg1)
   for var in var_tuple:
      print (var)
   return
 
# ����print_info ����
print_info( 10 )
print_info( 70, 60, 50 )

from sympy import pi, tan

# ʹ�÷��ż���
tan_pi_4 = tan(pi / 4)
deg_pi_3 = (pi / 3 * 180 / pi)

print(tan_pi_4)  # Output: 1
print(deg_pi_3)  # Output: 60
