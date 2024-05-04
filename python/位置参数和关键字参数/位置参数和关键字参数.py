# 位置参数和关键字参数

def receive_args(*args, **kwargs):
    print(f"args type is:{type(args)},value is: {args}")
    print(f"kwargs type is:{type(kwargs)}, value is:{kwargs}")


if __name__ == '__main__':
    receive_args(0, name="jyz")
