# -*- coding: gbk -*-
# Author: style_forever
# Date: 12
# Description: 

# Python 的装饰器是一个强大的工具，用于在不修改函数或方法的定义情况下，动态地修改或扩展其行为
# 日志记录：自动记录函数的调用信息，如输入参数、返回值等。
# 权限检查：在执行某个函数之前检查用户是否有权限执行该操作。
# 缓存：缓存函数的结果，以提高性能，避免重复计算。
# 性能测试：测量函数的执行时间，以评估性能。
# 输入验证：自动验证函数输入的有效性。

# 使用装饰器的好处
# 提高代码复用性：将通用的功能抽取到装饰器中，可以在多个函数上复用。
# 增强代码可读性：将附加逻辑与业务逻辑分开，使代码更清晰易懂。
# 简化功能扩展：可以在不修改原函数的情况下，轻松地扩展其功能。

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")  # 打印函数的调用信息
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")   # 打印函数的返回值
        return result
    return wrapper

@my_decorator
def say_hello(name):
    return f"Hello, {name}!"

say_hello("Alice")
