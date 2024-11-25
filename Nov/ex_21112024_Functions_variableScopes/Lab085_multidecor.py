def decorator1(func):
    def wrapper():
        print("d1")
        func()

    return wrapper()


def decorator2(func):
    def wrapper():
        print("d2")
        func()

    return wrapper()

@decorator1
@decorator2
def say_hello():
 print("hello")

say_hello()
