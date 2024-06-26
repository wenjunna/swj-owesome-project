# 你的第一个装饰器
# 装饰器 封装一个函数，并且用这样或者那样的方式来修改他的行为。
from functools import wraps


def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


@a_new_decorator
def a_function_requiring_decoration():
    """hey yo ! decorate me !"""
    print("I am the function which needs some decoration to remove my foul smell.")


a_function_requiring_decoration()
print(a_function_requiring_decoration.__name__)
