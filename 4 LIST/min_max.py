# min and max function
import random

number = [6,60,2]
numbers = []
# for i in range(0,12):
#     numbers.append(random.randint(0,1001))
# print(numbers)

# print(min(numbers))
# print(max(numbers))

def greatest_diff(l):
    return max(l)-min(l)
print(greatest_diff(numbers))