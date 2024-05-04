def receive_args(*args, **kwargs):
    print("args is:", args)
    print("kwargs is: ", kwargs)


if __name__ == '__main__':
    a = 0
    b = 1
    d = {"name": "jyz", "gender": "male"}
    receive_args(a, b, d)
    receive_args(a, b, **d)


# args本质是一个tuple，kwargs本质是dict；
# 传入关键字参数时，要么使用key=value形式传递；要么先定义dict再使用**dict传递。