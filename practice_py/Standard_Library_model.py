# -*- coding: gbk -*-
# Author: style_forever
# Date: 12
# Description: 


# Python ��׼��
# os ģ�飺os ģ���ṩ����������ϵͳ�����ĺ��������紴�����ƶ���ɾ���ļ���Ŀ¼���Լ����ʻ��������ȡ�

# sys ģ�飺sys ģ���ṩ���� Python ��������ϵͳ��صĹ��ܣ�����������İ汾��·�����Լ��� stdin��stdout �� stderr ��ص���Ϣ��

# time ģ�飺time ģ���ṩ�˴���ʱ��ĺ����������ȡ��ǰʱ�䡢��ʽ�����ں�ʱ�䡢��ʱ�ȡ�

# datetime ģ�飺datetime ģ���ṩ�˸��߼������ں�ʱ�䴦���������紦��ʱ��������ʱ���������ڲ�ȡ�

# random ģ�飺random ģ���ṩ������������ĺ���������������������������������еȡ�

# math ģ�飺math ģ���ṩ����ѧ�������������Ǻ���������������ָ�������������ȡ�

# re ģ�飺re ģ���ṩ��������ʽ�����������������ı��������滻���ָ�ȡ�

# json ģ�飺json ģ���ṩ�� JSON ����ͽ��뺯�������Խ� Python ����ת��Ϊ JSON ��ʽ������ JSON ��ʽ�н����� Python ����

# urllib ģ�飺urllib ģ���ṩ�˷�����ҳ�ʹ��� URL �Ĺ��ܣ����������ļ������� POST ���󡢴��� cookies �ȡ�




# ��������

# xml.etree.ElementTree ģ�飺xml.etree.ElementTree ģ���ṩ�˽��� XML �ĵ��Ĺ��ܣ����Խ� XML �ĵ�ת��Ϊ Element ���󣬲�ͨ�� Element ���������� XML �ĵ���

# csv ģ�飺csv ģ���ṩ�˶�ȡ��д�� CSV �ļ��Ĺ��ܣ����Խ��б�����ת��Ϊ CSV ��ʽ������ CSV ��ʽ�ж�ȡ�б����ݡ�

# sqlite3 ģ�飺sqlite3 ģ���ṩ�˷��� SQLite ���ݿ�Ĺ��ܣ�����ִ�� SQL ��䣬������ɾ�������롢���º�ɾ����¼�ȡ�

# hashlib ģ�飺hashlib ģ���ṩ�˸��ֹ�ϣ�㷨�ĺ��������Զ��ַ������м��ܣ�������� MD5 ��ϣֵ��SHA1 ��ϣֵ�ȡ�

# hmac ģ�飺hmac ģ���ṩ�˹�ϣ��Ϣ��֤�루HMAC���Ĺ��ܣ�����ʵ����Ϣ��������У�顣

# zlib ģ�飺zlib ģ���ṩ��ѹ���ͽ�ѹ�����ݵĺ���������ʵ�����ݵ�ѹ���ͽ�ѹ����

# bz2 ģ�飺bz2 ģ���ṩ�� bzip2 ѹ���ͽ�ѹ�����ݵĺ���������ʵ�����ݵ�ѹ���ͽ�ѹ����

# zipfile ģ�飺zipfile ģ���ṩ�˴����ͽ�ѹ ZIP �ļ��Ĺ��ܣ�����ʵ���ļ�����ͽ����

# smtplib ģ�飺smtplib ģ���ṩ�˷����ʼ��Ĺ��ܣ�����ʵ���ʼ��ķ��͡�

# email ģ�飺email ģ���ṩ�˴����ʼ��Ĺ��ܣ�����ʵ���ʼ��Ľ��������ɺͷ��͡�

# uuid ģ�飺uuid ģ���ṩ������ UUID �Ĺ��ܣ�����ʵ�� UUID �����ɡ�

# multiprocessing ģ�飺multiprocessing ģ���ṩ�˴������̵Ĺ��ܣ�����ʵ�ֶ���̱�̡�

# asyncio ģ�飺asyncio ģ���ṩ���첽��̵Ĺ��ܣ�����ʵ���첽 IO��

# logging ģ�飺logging ģ���ṩ����־��¼�Ĺ��ܣ�����ʵ����־�������

# unittest ģ�飺unittest ģ���ṩ�˵�Ԫ���ԵĹ��ܣ�����ʵ�ֵ�Ԫ���ԡ�

# argparse ģ�飺argparse ģ���ṩ�������в��������Ĺ��ܣ�����ʵ�������в����Ľ�����

# configparser ģ�飺configparser ģ���ṩ�������ļ������Ĺ��ܣ�����ʵ�������ļ��Ľ�����

# tkinter ģ�飺tkinter ģ���ṩ�˴��� GUI ����Ĺ��ܣ�����ʵ��ͼ���û����档

# turtle ģ�飺turtle ģ���ṩ�˻���ͼ�εĹ��ܣ�����ʵ��ͼ�εĻ��ơ�  


# ʱ������ģ��
import datetime

#��ȡ��ǰ���ں�ʱ��
current_datetime = datetime.datetime.now()
print(current_datetime)

# ��ȡ��ǰ����
current_date = datetime.date.today()
print(current_date)

# ��ʽ������
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)  # �����2023-07-17 15:30:45



# �ַ�������ƥ��
import re

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))  # �����['foot', 'fell', 'fastest']
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))  # �����cat in the hat


# �ļ�����
import os
print(os.getcwd())


#�ļ�ͨ���
import glob
print(glob.glob('./practice_py/*.py'))  # �����ǰĿ¼������.py�ļ�