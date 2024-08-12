# -*- coding: gbk -*-
# Author: style_forever
# Date: 12
# Description: Python ������
# 
# 
# Python ��������һ����4�֣��ֱ��ǣ�

# ������������

# L��Local�������ڲ㣬�����ֲ�����������һ������/�����ڲ���
# E��Enclosing���������˷Ǿֲ�(non-local)Ҳ��ȫ��(non-global)�ı�������������Ƕ�׺�����һ�����������ࣩ A �����ְ�����һ������ B ����ô���� B �е�������˵ A �е��������Ϊ nonlocal��
# G��Global������ǰ�ű�������㣬���統ǰģ���ȫ�ֱ�����
# B��Built-in���� �������ڽ��ı���/�ؼ��ֵȣ����������




# ȫ�ֱ����;ֲ�����
# �����ں����ڲ��ı���ӵ��һ���ֲ������򣬶����ں������ӵ��ȫ��������
# �ֲ�����ֻ���ں����ڲ����ʣ���ȫ�ֱ�����������������Χ�ڷ��ʡ�

#!/usr/bin/python3
 
total = 0 # ����һ��ȫ�ֱ���
# ��д����˵��
def sum( arg1, arg2 ):
    #����2�������ĺ�."
    total = arg1 + arg2 # total�������Ǿֲ�����.
    print ("�������Ǿֲ����� : ", total)
    return total
 
#����sum����
sum( 10, 20 )
print ("��������ȫ�ֱ��� : ", total)


# ���ڲ����������޸��ⲿ������ı���ʱ����Ҫ�õ� global �� nonlocal �ؼ����ˡ�

#!/usr/bin/python3
 
num = 1
def fun1():
    global num  # ��Ҫʹ�� global �ؼ�������
    print(num) 
    num = 123
    print(num)
fun1()
print(num)

# ���Ҫ�޸�Ƕ��������enclosing ����������ȫ���������еı�������Ҫ nonlocal �ؼ����ˣ�����ʵ����
#!/usr/bin/python3
 
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal�ؼ�������
        num = 100
        print(num)
    inner()
    print(num)
outer()