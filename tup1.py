a=("apple" , "orange" , "pea")

y=list(a)
y[1]="grapes"
a= tuple(y)
print(a)

#converts tuple into list
my_tup=(1 , 2 , 3 , 4, 5  , 8, 9  ,10 ,16)
new_tup=my_tup[1:5:3]
print(new_tup)

#negative slicing ka example

my_tup=( 10 , 20 , 40 , 60 , 70)
red_tup=my_tup[-1:-4:-2]
print(red_tup)


# max and min built in function


my_tup=( 1 , 2 , 3 , 4 , 5)
newtup=max(my_tup)
print(newtup)

#2

tup = (2 ,46, 3,44,5 )
new=min(tup)
print(new)

#3 length 

tup=( 12 , 33, 44,55 ,66,66 )
new=len(tup)
print(new)

#4 append func we cannot add elememt so first we have to make list


upi=(12,34,56,67)
nui=list(upi)
nui.append(56)
nui=tuple(nui)
print(nui)



my_list = [1, 2, 3]



# Inserting an element at a specific position
my_list.insert(1, 5)  # my_list becomes [1, 5, 2, 3, 4]
print

# Removing an element
my_list.remove(3)  # my_list becomes [1, 5, 2, 4]
