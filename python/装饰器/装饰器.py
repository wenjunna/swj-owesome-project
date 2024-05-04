# 装饰器
# https://www.runoob.com/w3cnote/python-func-decorators.html
# http://www.360doc.com/content/22/0602/21/5758241_1034304833.shtml

import time
def timmer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        stop = time.time()
        print(stop - start)
        return res

    return wrapper


# 在被装饰对象正上方的单独一行写 @装饰器名字
@timmer
def index(x, y, z):
    time.sleep(3)
    print("index %s %s %s" % (x, y, z))
    return 1


@timmer
def home(name):
    time.sleep(2)
    print("welcome %s to home page" % name)
    return 1


index(x=1, y=2, z=3)
res = home("egon")
print("返回值-->", res)
