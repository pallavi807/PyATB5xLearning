"""1. `The can't return -> non return`
2. They can return something / no return type and with argument
3. They have parameters
4. `They don't parameters / arguments`, argument+return type
"""
import math

from Nov.ex_07112024_Python_Basics.Lab007_maxNum import result


# non return
# no return type and no paramter/argument
def greet():
    print("hello")


greet()


# 2.no return type and with argument/para
def greet_by_name(name):
    print("hello,", name)


greet_by_name("pallavi")


# 3.no return type and with default argument(#positional argu)
def say_hello_default_arg(name="pallavi"):
    print("hello", name.upper())


say_hello_default_arg("kadam")
say_hello_default_arg()


def multiple_args(name1="a", name2="b"):
    print("mul ->", name1, name2)


multiple_args()
multiple_args(name1="pallavi")
multiple_args(name1="pallu", name2="kadam")
multiple_args(name2="kadam")
multiple_args("vaidehi")
multiple_args("vaidehi", "sarap")




# 4.argument+return type

def sum_of_two(a, b):
    return a + b

result = sum_of_two(4, 56)
print(result)

def sum_of_two_number_with_default(num1=100,num2=200):
    return num1+num2
result=sum_of_two_number_with_default(30,40)
print(result)
result=sum_of_two_number_with_default()
print(result)

