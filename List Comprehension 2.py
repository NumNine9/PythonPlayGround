a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
#I want 'n' for each 'n' in a IF 'n' is even

my_List = []
for n in a:
    if n%2==0:
        my_List.append(n)
print(my_List) 

# Same example using list comprehension

my_List2 = [n for n in a if n%2==0]
print(my_List2)