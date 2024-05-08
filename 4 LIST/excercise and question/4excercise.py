# filter odd even
# define a function
# input
# list ---> [1,2,3,4,5,6,7]
# output --->[[1,3,5,7],[2,4,6]]

# first odd even
# than put odd in another list and even in other list
# than concatnate these both list in a single list

n = int(input("Enter the size:"))
li = []
for i in range(0,n):
    nums = int(input("Enter the numbers:"))
    li.append(nums)
print(li)
def odd_even(l):
    odd = []
    even = []
    for i in l :
        if  i % 2 ==0:
            even.append(i)
        else:
            odd.append(i)
    output = [even,odd]
    return output
print(odd_even(li))
