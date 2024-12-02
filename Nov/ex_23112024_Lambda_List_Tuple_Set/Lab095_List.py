from Nov.ex_19112024_Functions.Lab075_real_args import pallavi

my_list = [1,2,3]

#indexing
print("element at index 0-",my_list[0])
print("element at index 1-",my_list[1])
print("element at index 2-",my_list[2])


#append()
#it will add object to the list in  the end.
my_list.append(4)
my_list.append(5)
print(my_list)

#extend() - append a new list
my_list.extend([7,8,10,9])
print(my_list)

#insert()
my_list.insert(1,'pallavi')
print(my_list)
print(len(my_list))

my_list[3]="amit"
print(my_list)

#remove()
my_list.remove("amit")
my_list.remove("pallavi")
print(my_list)
print("=====================")
#we can copy list
my_copy_list=my_list.copy()
print(my_list)
print(my_copy_list)
my_copy_list=my_list.sort()
print(my_list)
print(my_copy_list)