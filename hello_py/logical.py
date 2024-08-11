# -*- coding: gbk -*-
# Author: style_forever
# Date: 11
# Description: 




# if condition_1:
#     statement_block_1
# elif condition_2:
#     statement_block_2
# else:
#     statement_block_3


# Python 3.10 ������ match...case �������жϣ�����Ҫ��ʹ��һ������ if-else ���ж��ˡ�

# match ��Ķ���������� case ������ݽ���ƥ�䣬���ƥ��ɹ�����ִ��ƥ�䵽�ı��ʽ������ֱ��������_ ����ƥ��һ�С�
# match ������һ�����ʽ������ֵ����һ������case ������ʽ������һϵ��ģʽ���бȽϡ� ����������switch case ���ܲ�ͬ��һ���ǣ�match case ����break �����˳���ÿ��case �Ƕ������߼���

# case _: ������ C �� Java �е� default:�������� case ���޷�ƥ��ʱ��ƥ����������֤��Զ��ƥ��ɹ�
# �﷨��ʽ���£�

# match_object:
#     case_1:
#         expression_1
#         break
#     case_2:        
#         expression_2
#         break
#     case_3:
#         expression_3
#         break
#     case _:
#         expression_4
#         break


# �ٸ����ӣ�

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

my_status=400
print(http_error(400))



# while �ж�����(condition)��
#     ִ�����(statements)����
# ������ʾ���飬�����ж��У������뱣��һ�µ�������


#!/usr/bin/python3
 
var = 1
while var == 1 :  # ���ʽ��ԶΪ true
   num = int(input("����һ������  :"))
   print ("�������������: ", num)
 
print ("Good bye!")

# �����ʹ�� CTRL+C ���˳���ǰ������ѭ����

# ����ѭ���ڷ������Ͽͻ��˵�ʵʱ����ǳ�����


# for ѭ������(variable) in �ɵ�������(iterable)��
#     ִ�����(statements)����
#�ɵ����Ķ�������б�Ԫ�顢�ַ������ֵ�ȡ�

# ������ʾ���飬�����ж��У������뱣��һ�µ�������
# ������Χֵ������� range() ����ʹ�ã�
#!/usr/bin/python3
 
 
#range()��������һ���������д�0��ʼ����ָ�����ֽ�����������ָ������
# Ҳ����ʹ range() ��ָ�����ֿ�ʼ��ָ����ͬ������(���������Ǹ�������ʱ��Ҳ����'����'):
# range(0, 10, 3) ���ɵ������� 0 3 6 9
# range(5, -1, -2) ���ɵ������� 5 3 1


#  1 �� 5 ���������֣�
for number in range(1, 6):         
    print(number)                   
 
# ��������
# 1
# 2
# 3       
# 4
# 5
 
# �ַ���Ҳ����ʹ�� for ѭ����
for letter in "hello":                #�ַ���"hello"��һ���ɵ�������
    print(letter)
 
# ��������
# h
# e
# l
# l

# break ���������� for �� while ��ѭ���塣������ for �� while ѭ������ֹ���κζ�Ӧ��ѭ�� else �齫��ִ�С�
# continue ��䱻�������� Python ������ǰѭ�����е�ʣ����䣬Ȼ�����������һ��ѭ����