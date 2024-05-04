from functools import wraps


class logit(object):
    def __init__(self, logfile="out.log"):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)

            with open(self.logfile, 'a') as opened_file:
                opened_file.write(log_string + "\n")
            self.notify()
            return func(*args, **kwargs)

        return wrapped_function

    def notify(self):
        pass


class email_logit(logit):
    """
    一个logit的实现版本，可以在函数调用时发送email给管理员
    """

    def __init__(self, email="admin@myproject.com", *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        pass


@logit
def myfunc1():
    pass
