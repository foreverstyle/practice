
# -*- coding: gbk -*-
#������������仰����Ҫ


#���Բ���̳�
# Python �е����� ' ��˫���� " ʹ����ȫ��ͬ��
# ʹ��������(''' �� """)����ָ��һ�������ַ�����
# ת��� \��
# ��б�ܿ�������ת�壬ʹ�� r �����÷�б�ܲ�����ת�塣 �� r"this is a line with \n" �� \n ����ʾ�������ǻ��С�
# ���������弶���ַ������� "this " "is " "string" �ᱻ�Զ�ת��Ϊ this is string��
# �ַ��������� + �����������һ���� * ������ظ���
# Python �е��ַ���������������ʽ������������ 0 ��ʼ������������ -1 ��ʼ��
# Python �е��ַ������ܸı䡣
# Python û�е������ַ����ͣ�һ���ַ����ǳ���Ϊ 1 ���ַ�����
# �ַ�����Ƭ str[start:end]������ start������������Ƭ��ʼ��������end��������������Ƭ������������
# �ַ�������Ƭ���Լ��ϲ������� step���﷨��ʽ���£�str[start:end:step]

#!/usr/bin/python3
 
# ����[ͷ�±�:β�±�]

# ͷ�±��0��ʼ��β�±��-1��ʼ

str='123456789'
 
print(str)                 # ����ַ���
print(str[0:-1])           # �����һ���������ڶ����������ַ�
print(str[0])              # ����ַ�����һ���ַ�
print(str[2:5])            # ����ӵ�������ʼ�����������ַ�����������
print(str[2:])             # ����ӵ�������ʼ��������ַ�
print(str[1:5:2])          # ����ӵڶ�����ʼ���������ÿ��һ�����ַ�������Ϊ2��
#��һ����ͷ���ڶ�����β���������ǲ������������Ϊ���������ʾ����

print(str * 2)             # ����ַ�������
print(str + '���')         # �����ַ���
 
print('------------------------------')
 
print('hello\npython')      # ʹ�÷�б��(\)+nת�������ַ�
print(r'hello\npython')     # ���ַ���ǰ�����һ�� r����ʾԭʼ�ַ��������ᷢ��ת��


#!/usr/bin/python3
 
x="a"
y="b"
# �������
print( x )
print( y )
 
print('---------')
# ���������
print( x, end=" " )
print( y, end=" " )
print()


# eval() ������������ִ��һ���ַ������ʽ�������ر��ʽ��ֵ��
# �﷨��ʽ��eval(expression[, globals[, locals]])
# ���У�globals �� locals �ǿ�ѡ������ָ����ִ�б��ʽ�Ļ�����
# ��� globals �� locals ��û��ָ������Ĭ��ʹ�õ�ǰ��ȫ�ֺ;ֲ������ռ䡣
# ʾ����

#!/usr/bin/python3
 
a = 10
b = 20
c = eval("a + b")
print(c)  # ��� 30

# ע�⣺eval() ������ʹ�÷ǳ�Σ�գ���Ϊ������ִ��������룬�п��ܵ��´���ִ�еİ�ȫ���⡣

# �ַ�����ʽ����

#print ��Ĭ�ϻ��е� print ���������Ҫʵ�ֲ����е� print�������� end ����ָ������������ end=' '��

print("hello", end=" ")
print("world")  # �����hello world

# �ַ�����ʽ�����﷨��ʽ�ǣ�"{value1:format1}{value2:format2}...{valueN:formatN}"
# ���У�value ��Ҫ��ʽ����ֵ��format �Ǹ�ʽ���롣
# �����ĸ�ʽ�����У�
# - d������ decimal
# - f�������� float
# - s���ַ��� string
# - %���ٷֱ� percentage
# ʾ����

#!/usr/bin/python3
 
name = "Alice"
age = 25
score = 89.5
 
print("My name is {} and I am {} years old. My score is {:.2f}%.".format(name, age, score))
# �����My name is Alice and I am 25 years old. My score is 89.50%. 

# ���У�{:.2f} ��ʾ��ʽ��Ϊ��������������λС����


#�ַ����ڽ�����

str = "Hello, World!"

print(str.capitalize())  # ����ĸ��д
print(str.center(20, "*"))  # ���ж���
print(str.count("l"))  # ͳ���ַ����ִ���
print(str.find("l"))  # �����Ӵ���λ��      
print("".join(["1", "2", "3"]))  # �����ַ���
print(str.lower())  # ת��ΪСд
print(str.upper())  # ת��Ϊ��д
print(str.replace("l", "L"))  # �滻�ַ�
print(str.split())  # ���ո�ָ��ַ���
print(str.strip())  # ȥ�����˿ո�

print(len(str))  # �����ַ�������
print(str.index("l"))  # �����Ӵ���λ�ã�����Ҳ��������׳��쳣

#ʹ�� \r ʵ�ְٷֱȽ��ȣ�

import time  # ����timeģ�飬������ʱ

for i in range(101):  # ѭ��101�Σ���0��100
    print("\r{:3}%".format(i),end=' ')  # ��ӡ��ǰ���ȣ�\r���ڻص����ף�{:3}%��ʽ������ٷֱȣ�end=' '���ڲ�����
    time.sleep(0.05)  # ��ʱ0.05�룬ģ�����������