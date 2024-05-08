#  what is list comprehension?
# with the help of list comprehension we can create of list in one line 

# Q create a list of squares from 1 to 10 
# normal way
squares = []

for i in range(1,11):
    squares.append(i*i)
# print(squares)

# list comprehension

square2 = [i*i for i in range(1,11)]
# print(square2)

negative = [-i for i in range(1,11)]
# print(negative)

names = ['Ayush','Mohit','Rohit']
# new_list = []
# for name in names:
#     new_list.append(name[0])
# print(new_list)

new_list = [name[0] for name in names]
print(new_list)