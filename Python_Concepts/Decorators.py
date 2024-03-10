def my_dec(func1):
    def nowexec():
        print('Inside decorator')
        func1()
        print('In the end')
    return nowexec


@my_dec
def hello():
    print('Hello is executed')

hello()