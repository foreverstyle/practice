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


# Python 3.10 增加了 match...case 的条件判断，不需要再使用一连串的 if-else 来判断了。

# match 后的对象会依次与 case 后的内容进行匹配，如果匹配成功，则执行匹配到的表达式，否则直接跳过，_ 可以匹配一切。
# match 语句接受一个表达式并将其值与以一个或多个case 语句块形式给出的一系列模式进行比较。 和其他语言switch case 语句很不同的一点是，match case 不用break 进行退出，每个case 是独立的逻辑。

# case _: 类似于 C 和 Java 中的 default:，当其他 case 都无法匹配时，匹配这条，保证永远会匹配成功
# 语法格式如下：

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


# 举个例子：

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



# while 判断条件(condition)：
#     执行语句(statements)……
# 缩进表示语句块，可以有多行，但必须保持一致的缩进。


#!/usr/bin/python3
 
var = 1
while var == 1 :  # 表达式永远为 true
   num = int(input("输入一个数字  :"))
   print ("你输入的数字是: ", num)
 
print ("Good bye!")

# 你可以使用 CTRL+C 来退出当前的无限循环。

# 无限循环在服务器上客户端的实时请求非常有用


# for 循环变量(variable) in 可迭代对象(iterable)：
#     执行语句(statements)……
#可迭代的对象包括列表、元组、字符串、字典等。

# 缩进表示语句块，可以有多行，但必须保持一致的缩进。
# 整数范围值可以配合 range() 函数使用：
#!/usr/bin/python3
 
 
#range()函数生成一个整数序列从0开始，到指定数字结束，不包括指定数字
# 也可以使 range() 以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
# range(0, 10, 3) 生成的序列是 0 3 6 9
# range(5, -1, -2) 生成的序列是 5 3 1


#  1 到 5 的所有数字：
for number in range(1, 6):         
    print(number)                   
 
# 输出结果：
# 1
# 2
# 3       
# 4
# 5
 
# 字符串也可以使用 for 循环：
for letter in "hello":                #字符串"hello"是一个可迭代对象
    print(letter)
 
# 输出结果：
# h
# e
# l
# l

# break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
# continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。