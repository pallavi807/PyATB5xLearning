#write a program that will display lette grade
#for a given numerical score (eg, a,b,c,d,f)
# based on following grade scale
#a=90-100
#b=80-89
#c=70-79
#d= 60-69
#f=0-59

#logic buiding formula
#1=i/p---marks or score --int
#2=o/p --grade--str
score=int(input("enter your score \n"))
#rough logic
#score > 90 or <100 - "A"
#score >80 or <89 - "b

if  score >=90 and score<=100:
    print("grade is","A")
elif  score >=80 and score<=89:
    print("B")
elif score >=70 and score<=79:
    print("c")
elif score >=60 and score<=69:
    print("d")
elif score>100:
    print("superman")
else:print("you are fail")
