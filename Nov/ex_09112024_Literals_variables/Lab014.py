#write a program to take 2inputs from a user
#then sum the numbers
#sum= +
#sub=-
#mul=*
#div=/

""" Logic Building

 Step 1
 I/P -> num1, num2 -> int
 O/P -> sum - int, sub -> int, div -> float
 """ #multi comment



num1=int(input("enter your num1"))         #to take input from the user we use input function.
num2=int(input('enter your num2'))        #int() to convert str to int.
sum = num1+num2
print(sum)
print (type(num1))  #print(type(sum))
print (type(num2))

name=input("enter your name")
print ("Your name is",name)
print (type(name))


# Step 2 | Rough Logic
# Sum +, - , / ,*

  # as the num1,num2 are string sub,mul div is not possible of str
# so we need to convert str to int.
# str -> int
int()


# Step 3
sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print("Sum is : ", sum)
print("Sub is : ", sub)
print("Mul is : ", mul)
print("Div is : ", div)





