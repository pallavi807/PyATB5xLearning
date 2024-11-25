pb_global_b=12   #----global variable
def my_function():
    pb_a=10 #----local variable
    print(pb_a)
    print(pb_global_b)

#print(pb_a)//name"pb_a"is not defined
print(pb_global_b)  #global var can be used outside but local cnt.
my_function()