# We use enumerate function with for loop to track postion of our item in iterable 



# How we can do this without enumerate function
names = ['abc','abcdef','ayush','santosh']
# # pos = 0 
# for name in names:
#     print(f"{pos} ----->{name}")
#     pos += 1



# With enumerate function
for pos, name in enumerate(names):
    print(f"{pos}----->{name}")

def list_take(l,s):
    for postion , name in enumerate(l):
        if name == s:
            return postion
    return -1

print(list_take(names,'ayush'))
