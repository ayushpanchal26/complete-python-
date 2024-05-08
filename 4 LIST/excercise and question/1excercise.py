# define a function which will take list containing number as input 
# and return list containing square of every elements
n = int(input("Enter how many number you want to add"))
list1 = []
for i in range(0,n):
    li = int(input("enter any number"))
    list1.append(li)
print(list1)
def square_list(l):
    square = []
    for i in l:
        square.append(i*i)
    return square
print(square_list(list1))
# finally made it perfection

