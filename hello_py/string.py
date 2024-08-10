
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


# eval() 函数可以用来执行一个字符串表达式，并返回表达式的值。
# 语法格式：eval(expression[, globals[, locals]])
# 其中，globals 和 locals 是可选参数，指定了执行表达式的环境。
# 如果 globals 和 locals 都没有指定，则默认使用当前的全局和局部命名空间。
# 示例：

#!/usr/bin/python3
 
a = 10
b = 20
c = eval("a + b")
print(c)  # 输出 30

# 注意：eval() 函数的使用非常危险，因为它可以执行任意代码，有可能导致代码执行的安全问题。

# 字符串格式化：

#print 是默认换行的 print 函数，如果要实现不换行的 print，可以用 end 参数指定结束符，如 end=' '。

print("hello", end=" ")
print("world")  # 输出：hello world

# 字符串格式化的语法格式是："{value1:format1}{value2:format2}...{valueN:formatN}"
# 其中，value 是要格式化的值，format 是格式代码。
# 常见的格式代码有：
# - d：整数 decimal
# - f：浮点数 float
# - s：字符串 string
# - %：百分比 percentage
# 示例：

#!/usr/bin/python3
 
name = "Alice"
age = 25
score = 89.5
 
print("My name is {} and I am {} years old. My score is {:.2f}%.".format(name, age, score))
# 输出：My name is Alice and I am 25 years old. My score is 89.50%. 

# 其中，{:.2f} 表示格式化为浮点数，保留两位小数。


#字符串内建函数

str = "Hello, World!"

print(str.capitalize())  # 首字母大写
print(str.center(20, "*"))  # 居中对齐
print(str.count("l"))  # 统计字符出现次数
print(str.find("l"))  # 查找子串的位置      
print("".join(["1", "2", "3"]))  # 连接字符串
print(str.lower())  # 转换为小写
print(str.upper())  # 转换为大写
print(str.replace("l", "L"))  # 替换字符
print(str.split())  # 按空格分割字符串
print(str.strip())  # 去除两端空格

print(len(str))  # 计算字符串长度
print(str.index("l"))  # 查找子串的位置，如果找不到，会抛出异常

#使用 \r 实现百分比进度：

import time  # 导入time模块，用于延时

for i in range(101):  # 循环101次，从0到100
    print("\r{:3}%".format(i),end=' ')  # 打印当前进度，\r用于回到行首，{:3}%格式化输出百分比，end=' '用于不换行
    time.sleep(0.05)  # 延时0.05秒，模拟进度条更新