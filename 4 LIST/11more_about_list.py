# genrate lists with range function
# something about pop method
# index method
# pass list to a function


# 1
numbers = list(range(1,11))
# print(numbers)

# 2 
# print(numbers.pop())
# popped_item = numbers.pop()
# print(numbers)
num = [1,2,3,4,5,7,8,9,10,1,5,7,8,1]
# 3
# print(num.index('word',9))

# first jo find karna and second kha sai start karna and third wala stop kha karna
def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(num))
