#write a pro to calculate even and odd

def find_even_odd(num):
  if num %2==0:
    print("even")
  else:
    print("odd")
find_even_odd(5)

n=int(input("enter number\n"))
find_even_odd=lambda num: "even" if num%2==0 else "odd"
#print(find_even_odd(17))
#print(find_even_odd(10))
print(find_even_odd(n))