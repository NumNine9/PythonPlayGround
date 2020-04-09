a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
print(my_list)

#using list compreension

my_list2 = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list2)