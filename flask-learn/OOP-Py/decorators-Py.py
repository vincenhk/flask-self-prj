# def hellow():
#     return "Hello World!"
#
# def other(func):
#     print("Same others code")
#     print(func())
#
# other(hellow)

def new_decorator(func):
    def wrapper():
        print("some code before excecuting decorator")
        func()
        print("some code after excecuting decorator")

    return wrapper()


@new_decorator
def func_need_decorator():
    print("need decorator")


func_need_decorator()
