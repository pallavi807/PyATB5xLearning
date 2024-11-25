def add_security(func):
    def wrapper():
        print("1.before the function")
        print("2.add helmet")
        func()  # drive scooty
        print("3.after the function")
        print("4.secure driving")
    return wrapper()      #wrapper only


@add_security     #this name can be anything
def drive_scooty():
    print("normal function!!")
    print("I am driving a scooty")
