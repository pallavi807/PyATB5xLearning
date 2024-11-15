# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is
# equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.
"""
s1=int(input("enter lenth of first side :"))
s2=int(input("enter lenth of second side: "))
s3=int(input("enter lenth of third side: "))

if s1==s2 and s1==s3 and s2==s3:
    print("All sides are equal","equilateral")
elif s1==s2 and s1!=s3 or  s1==s3 and s2!=s3 or s2==s3 and s1!=s2:
    print("isosceles")
elif s1!=s2 and s1!=s3 or s1!=s3 and s2!=s3 :
    print("scalene")
"""
side1=6
side2=10
side3=10
if side1==side2 and side1==side3 and side2==side2:
    print("equilateral")
elif side1==side2 or side1==side3 or side3==side2:
    print("isosceles")
else:print("scalene")
