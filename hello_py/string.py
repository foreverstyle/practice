
# -*- coding: gbk -*-
#！！！！！这句话很重要


#来自菜鸟教程
# Python 中单引号 ' 和双引号 " 使用完全相同。
# 使用三引号(''' 或 """)可以指定一个多行字符串。
# 转义符 \。
# 反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。 如 r"this is a line with \n" 则 \n 会显示，并不是换行。
# 按字面意义级联字符串，如 "this " "is " "string" 会被自动转换为 this is string。
# 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
# Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
# Python 中的字符串不能改变。
# Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
# 字符串切片 str[start:end]，其中 start（包含）是切片开始的索引，end（不包含）是切片结束的索引。
# 字符串的切片可以加上步长参数 step，语法格式如下：str[start:end:step]

#!/usr/bin/python3
 
# 变量[头下标:尾下标]

# 头下标从0开始，尾下标从-1开始

str='123456789'
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第六个的字符（不包含）
print(str[2:])             # 输出从第三个开始后的所有字符
print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
#第一个是头，第二个是尾，第三个是步长，如果步长为负数，则表示逆序

print(str * 2)             # 输出字符串两次
print(str + '你好')         # 连接字符串
 
print('------------------------------')
 
print('hello\npython')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\npython')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

#!/usr/bin/python3
 
input("\n\n按下 enter 键后退出。")

#!/usr/bin/python3
 
x="a"
y="b"
# 换行输出
print( x )
print( y )
 
print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()