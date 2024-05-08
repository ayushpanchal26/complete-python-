# create your first genrator with genrator function 
# 1. genrator function
# 2. genrator comprehension

def nums(n):
    for i in range(1,n+1):
        yield i 

numbers = nums(10)

for num in numbers:
    if num<=5:
       print(num)
    else:
        break

# generator does not genrate all items in once it genrates the item only when it is required 
print("-------")
for num in numbers:
    print(num)