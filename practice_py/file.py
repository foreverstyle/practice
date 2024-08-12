# -*- coding: gbk -*-
# Author: style_forever
# Date: 12
# Description: 

# open() 方法用于打开一个文件，并返回文件对象。
# 语法：open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# 参数：
# file：要打开的文件名。
# mode：打开文件的模式，默认是只读模式'r'。
# buffering：设置缓冲区大小。
# encoding：文件编码。
# errors：指定如何处理编码错误。
# newline：指定行结束符。
# closefd：如果 closefd 为 False，那么文件描述符将不会关闭。
# opener：指定打开文件使用的函数。


# file.close()
# 关闭文件。关闭后文件不能再进行读写操作。

# file.read([size])
# 从文件读取指定的字节数，如果未给定或为负则读取所有。


# file.readline([size])
# 从文件读取一行内容，包括行结束符，如果未给定或为负则读取所有。


# file.readlines([sizehint])
# 读取所有行并返回列表，如果未给定或为负则读取所有。


# file.seek(offset, whence=0)
# 移动文件读取指针到指定位置。
# 参数：
# offset：偏移量，相对于 whence 位置。
# whence：起始位置，0 表示文件开头，1 表示当前位置，2 表示文件末尾。


# file.tell()
# 返回当前文件读取指针的位置。


# file.write(string)
# 向文件写入字符串。


# file.writelines(sequence)
# 向文件写入序列的每一项。