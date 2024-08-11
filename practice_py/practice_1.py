# -*- coding: gbk -*-
# Author: style_forever
# Date: 11
# Description: 



#!/usr/bin/python3
 
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=',')  # 打印出斐波纳契数列不换行
    a, b = b, a+b   # 计算下一个数