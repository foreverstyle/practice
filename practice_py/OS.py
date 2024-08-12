# -*- coding: gbk -*-
# Author: style_forever
# Date: 12
# Description: 

# Python �� os ģ���ṩ�������ϵͳ���н�����һЩ���ܣ�ʹ�������ִ�������ϵͳ��ص��������ļ���Ŀ¼�����������������ʡ����̹���ȡ����� Python ��׼���һ���֣��ṩ�˿�ƽ̨�Ĳ���ϵͳ�ӿڡ�

import os

# 1. ����һ����Ϊ myfile.txt ���ļ���д��һЩ����
with open("myfile.txt", 'w') as file:   # ��һ���ļ�������ļ������ڣ����ᱻ����������ļ��Ѵ��ڣ�����ļ����ݡ�
    file.write("This is a test file.")

# 2. ɾ���ļ�
# try:
#     os.remove("myfile.txt")
#     print("File deleted successfully.")
# except FileNotFoundError:
#     print("File not found.")
# except PermissionError:
#     print("Permission denied.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")




# 1. �ļ���Ŀ¼����
# Ŀ¼��Ҳ��Ϊ�ļ��У���һ��������֯�͹����ļ��Ľṹ��Ŀ¼�����������ݣ����ǰ����ļ���������Ŀ¼�����û�ָ�롣



# ����ϵͳ���ļ��Ĳ�����Ҫ�д�����ɾ�������������ƶ������Ƶȣ�Python �� os ģ���ṩ����Ӧ�ĺ��������Է���ض��ļ���Ŀ¼���в�����


# 1.1 ������ɾ��Ŀ¼

import os

# ����Ŀ¼
# os.mkdir('new_directory')  # ��������Ŀ¼
# os.makedirs('parent_directory/child_directory')  # �������Ŀ¼

# ɾ��Ŀ¼
# os.rmdir('new_directory')  # ɾ������Ŀ¼
# os.removedirs('parent_directory/child_directory')  # ɾ�����Ŀ¼



# 1.2 �г�Ŀ¼����
files = os.listdir('hello_py')  # �г���ǰĿ¼�е��ļ���Ŀ¼
print(files)



# 1.3 ���������ƶ��ļ���Ŀ¼
# os.rename('old_name.txt', 'new_name.txt')  # �������ļ�
# os.rename('source_file.txt', 'destination_directory/destination_file.txt')  # �ƶ��ļ�



# # 1.4 ɾ���ļ�
# os.remove('file_to_delete.txt')  # ɾ���ļ�


# 2.·������:

# 2.1 ��ȡ��ǰ����Ŀ¼�͸��Ĺ���Ŀ¼

current_dir = os.getcwd()  # ��ȡ��ǰ����Ŀ¼
print(current_dir)

# os.chdir('/path/to/directory')  # ���Ĺ���Ŀ¼

# 2.2 �����ļ�·��:
# path = os.path.join('new_directory', 'myfile.txt')  # ����Ŀ¼���ļ���
# print(path)

# 2.3 �����ļ�������չ��:
# filename, file_extension = os.path.splitext('file.txt')
# print(filename)  # ���: file
# print(file_extension)  # ���: .txt


#3 ��ȡ��������:

# home_dir = os.getenv('HOME')  # ��ȡ�������� 'HOME' ��ֵ
# print(home_dir)

#4 ����ϵͳ��Ϣ:

# os_name = os.name  # ��ȡ����ϵͳ���� ('posix', 'nt' ��) nt ��ʾ Windows ����ϵͳ posix ��ʾ Linux ����ϵͳ
# print(os_name)

# platform = os.uname()  # ��ȡƽ̨��Ϣ����ĳЩ����ϵͳ�п��ã�
# print(platform)


#5 ִ��ϵͳ����:

# os.system('echo Hello, World!')
