# 在函数中定义函数

def hi(name="yasoob"):
    print("now you are inside the hi() function.")

    def greet():
        return "name you are in the greet() function."

    def welcome():
        return "now you are in the welcome() function."

    print(greet())
    print(welcome())
    print("now you are back in the hi() function")


hi()
