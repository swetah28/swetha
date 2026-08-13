def outer(a):
    def inner(b):
        print(a+b)
    return inner
x=outer(20)
x(10)
x(15)