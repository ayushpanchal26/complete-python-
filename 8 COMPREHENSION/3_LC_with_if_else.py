# list comprehension with if else
nums = [1,2,3,4,5,6,7,8,9,10]
new = []
for i in nums:
    if i%2 == 0:
        new.append(i*2)
    else:
        new.append(-i)
print(new)

new_list = [i*2 if i%2 == 0 else -i for i in nums]
print(new_list)
# if we want to use if and else both than we will use it in starting
        