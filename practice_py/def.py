# -*- coding: gbk -*-
# Author: style_forever
# Date: 12
# Description: 

# 可更改(mutable)与不可更改(immutable)对象
# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

# 不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。

# 可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。


# python 函数的参数传递：

# 不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。

# 可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响

def change(a):
    print(id(a))   # 指向的是同一个对象
    a=10
    print(id(a))   # 一个新对象
 
a=1
print(id(a))
change(a)

#!/usr/bin/python3
 
# 可写函数说明
def change_me( my_list ):
   "修改传入的列表"
   my_list.extend([1,2,3,4])
   print ("函数内取值: ", my_list)
   return
 
# 调用change_me函数
my_list = [10,20,30]
change_me( my_list )
print ("函数外取值: ", my_list)

# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
# 加了两个星号 ** 的参数会以字典的形式导入
# 如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。如下实例：

#!/usr/bin/python3
 
# 可写函数说明
def print_info( arg1, *var_tuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   for var in var_tuple:
      print (var)
   return
 
# 调用print_info 函数
print_info( 10 )
print_info( 70, 60, 50 )

from sympy import pi, tan

# 使用符号计算
tan_pi_4 = tan(pi / 4)
deg_pi_3 = (pi / 3 * 180 / pi)

print(tan_pi_4)  # Output: 1
print(deg_pi_3)  # Output: 60
