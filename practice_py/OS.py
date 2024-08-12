# -*- coding: gbk -*-
# Author: style_forever
# Date: 12
# Description: 

# Python 的 os 模块提供了与操作系统进行交互的一些功能，使得你可以执行与操作系统相关的任务，如文件和目录操作、环境变量访问、进程管理等。它是 Python 标准库的一部分，提供了跨平台的操作系统接口。

import os

# 1. 创建一个名为 myfile.txt 的文件并写入一些内容
with open("myfile.txt", 'w') as file:   # 打开一个文件。如果文件不存在，它会被创建。如果文件已存在，清空文件内容。
    file.write("This is a test file.")

# 2. 删除文件
# try:
#     os.remove("myfile.txt")
#     print("File deleted successfully.")
# except FileNotFoundError:
#     print("File not found.")
# except PermissionError:
#     print("Permission denied.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")




# 1. 文件和目录操作
# 目录（也称为文件夹）是一个用于组织和管理文件的结构。目录本身不包含数据，而是包含文件和其他子目录的引用或指针。



# 操作系统对文件的操作主要有创建、删除、重命名、移动、复制等，Python 的 os 模块提供了相应的函数，可以方便地对文件和目录进行操作。


# 1.1 创建和删除目录

import os

# 创建目录
# os.mkdir('new_directory')  # 创建单层目录
# os.makedirs('parent_directory/child_directory')  # 创建多层目录

# 删除目录
# os.rmdir('new_directory')  # 删除单层目录
# os.removedirs('parent_directory/child_directory')  # 删除多层目录



# 1.2 列出目录内容
files = os.listdir('hello_py')  # 列出当前目录中的文件和目录
print(files)



# 1.3 重命名和移动文件和目录
# os.rename('old_name.txt', 'new_name.txt')  # 重命名文件
# os.rename('source_file.txt', 'destination_directory/destination_file.txt')  # 移动文件



# # 1.4 删除文件
# os.remove('file_to_delete.txt')  # 删除文件


# 2.路径操作:

# 2.1 获取当前工作目录和更改工作目录

current_dir = os.getcwd()  # 获取当前工作目录
print(current_dir)

# os.chdir('/path/to/directory')  # 更改工作目录

# 2.2 构建文件路径:
# path = os.path.join('new_directory', 'myfile.txt')  # 连接目录和文件名
# print(path)

# 2.3 分离文件名和扩展名:
# filename, file_extension = os.path.splitext('file.txt')
# print(filename)  # 输出: file
# print(file_extension)  # 输出: .txt


#3 获取环境变量:

# home_dir = os.getenv('HOME')  # 获取环境变量 'HOME' 的值
# print(home_dir)

#4 操作系统信息:

# os_name = os.name  # 获取操作系统名称 ('posix', 'nt' 等) nt 表示 Windows 操作系统 posix 表示 Linux 操作系统
# print(os_name)

# platform = os.uname()  # 获取平台信息（在某些操作系统中可用）
# print(platform)


#5 执行系统命令:

# os.system('echo Hello, World!')
