# 地址不变
# g_b = {"num1": 1, "num2": 2}
# print("t0", id(g_b), g_b)
#
#
# # global g_b
#
# # 测试三个服务以及三个函数是否使用同一个g_b
#
# def t1(num):
#     global g_b
#     g_b["num2"] += num
#     print("t1", id(g_b), g_b)
#     return g_b
#
#
# def t2(num):
#     global g_b
#     g_b["num2"] += num * num
#     print("t2", id(g_b), g_b)
#     return g_b
#
#
# def t3(num):
#     global g_b
#     g_b["num2"] += num / 2
#     print("t3", id(g_b), g_b)
#     return g_b
#
#
# 地址变化
g_b = 3

# 测试三个服务以及三个函数是否使用同一个g_b

def t1(num):
    global g_b
    g_b += num
    print("t1", id(g_b), g_b)
    return str(g_b)


def t2(num):
    global g_b
    g_b += num * num
    print("t2", id(g_b), g_b)
    return str(g_b)


def t3(num):
    global g_b
    g_b += num / 2
    print("t3", id(g_b), g_b)
    return str(g_b)

# t1()
# t2()
# t3()
# print("t0",id(g_b),g_b)
