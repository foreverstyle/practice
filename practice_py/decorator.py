# -*- coding: gbk -*-
# Author: style_forever
# Date: 12
# Description: 

# Python ��װ������һ��ǿ��Ĺ��ߣ������ڲ��޸ĺ����򷽷��Ķ�������£���̬���޸Ļ���չ����Ϊ
# ��־��¼���Զ���¼�����ĵ�����Ϣ�����������������ֵ�ȡ�
# Ȩ�޼�飺��ִ��ĳ������֮ǰ����û��Ƿ���Ȩ��ִ�иò�����
# ���棺���溯���Ľ������������ܣ������ظ����㡣
# ���ܲ��ԣ�����������ִ��ʱ�䣬���������ܡ�
# ������֤���Զ���֤�����������Ч�ԡ�

# ʹ��װ�����ĺô�
# ��ߴ��븴���ԣ���ͨ�õĹ��ܳ�ȡ��װ�����У������ڶ�������ϸ��á�
# ��ǿ����ɶ��ԣ��������߼���ҵ���߼��ֿ���ʹ����������׶���
# �򻯹�����չ�������ڲ��޸�ԭ����������£����ɵ���չ�书�ܡ�

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")  # ��ӡ�����ĵ�����Ϣ
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")   # ��ӡ�����ķ���ֵ
        return result
    return wrapper

@my_decorator
def say_hello(name):
    return f"Hello, {name}!"

say_hello("Alice")
