def outer_functions():
    var1=30 #local

    def inner_function():
     print(var1)


    def inner_function2():
         print(var1)

    inner_function()
    inner_function2()


outer_functions()