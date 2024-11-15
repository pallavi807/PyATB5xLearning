#program to fine max btwn number
#logic building
#step1
#i/p,o/p
num1=int(input("enter your num 1\n")) #5 10 1
num2=int(input("enter your num 2\n")) #3 12 2
num3=int(input("enter your num 3\n")) #2 11 3
#step2
#rough logic
#case1:
#num1>num2 ->num1  5>3
 #num1>num3 _>num1  5>2
#case2:
#num2>num1 ->num2   12>10
#num2>num3 -> num2   12>11

#case3: num3

if num1>num2 and num1>num3 :
    print("max is", num1)
elif num2>num1 and num2>num3:
    print("max is", num2)
else:
    print("max is ",num3)

