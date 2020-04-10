li = [3,7,6,3,5,2,9,8,1,4]

new_li = sorted(li) #this sorted func can return a value therefore it can be assigned to an variable

print('Sorted list :\t',new_li)

print('Unsorted list :\t',li)

li.sort() #this sort method returns a none therefore can not be assigned to a variable
print('\t\t',li)    #the \t\t is just to align the output

new_li = sorted(li, reverse=True) #this is to sort in descending order
print('Sorted list :\t',new_li)

li = [-4,-3,-6,2,1,5]

s_li = sorted(li, key=abs) #getting the absolute values of a list

print('\t\t',s_li)

class Employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    
    def __repr__(self):
        return '{},{},${}'.format(self.name,self.age,self.salary)
e1 = Employee('Carl',37,70000)
e2 = Employee('Sarah',29,80000)
e3 = Employee('John',43,90000)

#when sorting objects always use keys
'''
employee = [e1,e2,e3]
s_employee = sorted(employee) #it will not work 
print(s_employee)
'''
employees = [e1,e2,e3]
def e_sort(emp):
    return emp.name

s_employees = sorted(employees, key =e_sort,reverse=True) #it should sort according to the custom func
print(s_employees)

