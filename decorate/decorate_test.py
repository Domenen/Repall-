
def h2_wrap(func):
    def func_wrapper(param):
        return "<h2>" + func(param) + "</h2>"
    return func_wrapper
    
def h1_wrap(func):
    def func_wrapper(param):
        return "<h1>" + func(param) + "</h1>"
    return func_wrapper


@h2_wrap
def say_hi(name):
    return "Привет, " + name.capitalize()

print(say_hi("Арсений"))

