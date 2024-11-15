#write a pro to take user age and
#let him know if he can go to club
#21

#logic building formula
#step 1
#i/p,o/p

#step2
#rough logic, (brute force)
#age>21 , -- print can go
#age<21 , -- print cant go

#step3 Logic
age=int(input("enter your age\n"))
#age=int(age)

if age>=21:
    print("can go")
else:
    print("cant go")
    #step  4 . check for edge cases
    #neg value or high value pro will break
    #if alphanumeric value

