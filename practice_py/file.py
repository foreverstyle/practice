# -*- coding: gbk -*-
# Author: style_forever
# Date: 12
# Description: 

# open() �������ڴ�һ���ļ����������ļ�����
# �﷨��open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# ������
# file��Ҫ�򿪵��ļ�����
# mode�����ļ���ģʽ��Ĭ����ֻ��ģʽ'r'��
# buffering�����û�������С��
# encoding���ļ����롣
# errors��ָ����δ���������
# newline��ָ���н�������
# closefd����� closefd Ϊ False����ô�ļ�������������رա�
# opener��ָ�����ļ�ʹ�õĺ�����


# file.close()
# �ر��ļ����رպ��ļ������ٽ��ж�д������

# file.read([size])
# ���ļ���ȡָ�����ֽ��������δ������Ϊ�����ȡ���С�


# file.readline([size])
# ���ļ���ȡһ�����ݣ������н����������δ������Ϊ�����ȡ���С�


# file.readlines([sizehint])
# ��ȡ�����в������б����δ������Ϊ�����ȡ���С�


# file.seek(offset, whence=0)
# �ƶ��ļ���ȡָ�뵽ָ��λ�á�
# ������
# offset��ƫ����������� whence λ�á�
# whence����ʼλ�ã�0 ��ʾ�ļ���ͷ��1 ��ʾ��ǰλ�ã�2 ��ʾ�ļ�ĩβ��


# file.tell()
# ���ص�ǰ�ļ���ȡָ���λ�á�


# file.write(string)
# ���ļ�д���ַ�����


# file.writelines(sequence)
# ���ļ�д�����е�ÿһ�