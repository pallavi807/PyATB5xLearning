#create a pro to sum of three number from the user input.
#if user doesnt enter any number ,use default as 100, 200,300
from Nov.ex_19112024_Functions.Lab071_userdefined_Type import result

num1=int(input("enter num1\n"))
num2=int(input("enter num2\n"))
num3=int(input("enter num3\n"))

def sum_of_three_number(n1=100,n2=200,n3=300):
    return int(n1 + n2 + n3)

result=sum_of_three_number(num1,num2,num3)
print(result)

result2=sum_of_three_number()
print(result2)
result2=sum_of_three_number()
result2=sum_of_three_number(10)
result2=sum_of_three_number(10,20)
result2=sum_of_three_number(10,20,30)
print(result2)