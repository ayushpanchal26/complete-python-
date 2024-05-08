#define a function which will take list as a agrument and this function will return a reversed list

#example 
#[1,2,3,4] --> [4,3,2,1]

n = int(input("Enter the number of list:"))
list1 = []
for i in range(0,n):
    inp = int(input("Enter the list members:"))
    list1.append(inp)
print(list1)
def reverse(l):
    popp = []
    for i in range(len(l)):
        # popp.append(list1.pop())
        popp.append(list1.pop())
    return popp
    
print(reverse(list1))
