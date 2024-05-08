# common elements finder function
# define a function which takes 2 list as input and return a list
# which contains common elements of both lists

# example
# input ---> [1,2,5,8],[1,2,7,6]
# output ---> [1,2]

# solution
# take input of two list
# now compare the list and if common than put it in the temporary list
n1 = int(input("Enter size of list1:"))
n2 = int(input("Enter size of list2:"))
list1 = []
list2 = []
for i in range(0,n1):
    nums_for_l1 = int(input("Enter:"))
    list1.append(nums_for_l1)
print(list1)
for i in range(0,n2):
    nums_for_l2 = int(input("Enter:"))
    list2.append(nums_for_l2)
print(list2)

def common(l1,l2):
    temp = []
    for i in l1:
        if i in l2:
            temp.append(i)
    return temp

print(common(list1,list2))
