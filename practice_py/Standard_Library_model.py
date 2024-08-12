# -*- coding: gbk -*-
# Author: style_forever
# Date: 12
# Description: 


# Python 标准库
# os 模块：os 模块提供了许多与操作系统交互的函数，例如创建、移动和删除文件和目录，以及访问环境变量等。

# sys 模块：sys 模块提供了与 Python 解释器和系统相关的功能，例如解释器的版本和路径，以及与 stdin、stdout 和 stderr 相关的信息。

# time 模块：time 模块提供了处理时间的函数，例如获取当前时间、格式化日期和时间、计时等。

# datetime 模块：datetime 模块提供了更高级的日期和时间处理函数，例如处理时区、计算时间差、计算日期差等。

# random 模块：random 模块提供了生成随机数的函数，例如生成随机整数、浮点数、序列等。

# math 模块：math 模块提供了数学函数，例如三角函数、对数函数、指数函数、常数等。

# re 模块：re 模块提供了正则表达式处理函数，可以用于文本搜索、替换、分割等。

# json 模块：json 模块提供了 JSON 编码和解码函数，可以将 Python 对象转换为 JSON 格式，并从 JSON 格式中解析出 Python 对象。

# urllib 模块：urllib 模块提供了访问网页和处理 URL 的功能，包括下载文件、发送 POST 请求、处理 cookies 等。




# 第三方库

# xml.etree.ElementTree 模块：xml.etree.ElementTree 模块提供了解析 XML 文档的功能，可以将 XML 文档转换为 Element 对象，并通过 Element 对象来操作 XML 文档。

# csv 模块：csv 模块提供了读取和写入 CSV 文件的功能，可以将列表数据转换为 CSV 格式，并从 CSV 格式中读取列表数据。

# sqlite3 模块：sqlite3 模块提供了访问 SQLite 数据库的功能，可以执行 SQL 语句，创建、删除表、插入、更新和删除记录等。

# hashlib 模块：hashlib 模块提供了各种哈希算法的函数，可以对字符串进行加密，例如计算 MD5 哈希值、SHA1 哈希值等。

# hmac 模块：hmac 模块提供了哈希消息认证码（HMAC）的功能，可以实现消息的完整性校验。

# zlib 模块：zlib 模块提供了压缩和解压缩数据的函数，可以实现数据的压缩和解压缩。

# bz2 模块：bz2 模块提供了 bzip2 压缩和解压缩数据的函数，可以实现数据的压缩和解压缩。

# zipfile 模块：zipfile 模块提供了创建和解压 ZIP 文件的功能，可以实现文件打包和解包。

# smtplib 模块：smtplib 模块提供了发送邮件的功能，可以实现邮件的发送。

# email 模块：email 模块提供了处理邮件的功能，可以实现邮件的解析、生成和发送。

# uuid 模块：uuid 模块提供了生成 UUID 的功能，可以实现 UUID 的生成。

# multiprocessing 模块：multiprocessing 模块提供了创建进程的功能，可以实现多进程编程。

# asyncio 模块：asyncio 模块提供了异步编程的功能，可以实现异步 IO。

# logging 模块：logging 模块提供了日志记录的功能，可以实现日志的输出。

# unittest 模块：unittest 模块提供了单元测试的功能，可以实现单元测试。

# argparse 模块：argparse 模块提供了命令行参数解析的功能，可以实现命令行参数的解析。

# configparser 模块：configparser 模块提供了配置文件解析的功能，可以实现配置文件的解析。

# tkinter 模块：tkinter 模块提供了创建 GUI 界面的功能，可以实现图形用户界面。

# turtle 模块：turtle 模块提供了绘制图形的功能，可以实现图形的绘制。  


# 时间日期模块
import datetime

#获取当前日期和时间
current_datetime = datetime.datetime.now()
print(current_datetime)

# 获取当前日期
current_date = datetime.date.today()
print(current_date)

# 格式化日期
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)  # 输出：2023-07-17 15:30:45



# 字符串正则匹配
import re

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))  # 输出：['foot', 'fell', 'fastest']
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))  # 输出：cat in the hat


# 文件操作
import os
print(os.getcwd())


#文件通配符
import glob
print(glob.glob('./practice_py/*.py'))  # 输出当前目录下所有.py文件