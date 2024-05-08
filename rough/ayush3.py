# # f1 = ['orange','apple','pear']
# f1 = ['banana','kiwi','apple','banana']
# # print(f1 is f2) # is check whether the address is same or not
# # print(f1 == f2) # == check whether the list or any vairables values are same or not

# fruits = ['orange','apple','pear','banana','kiwi']

# # for loop
# for fruit in fruits:
#     print(fruit)
# print("------>>>>><<<<<<------")
# i = 0
# while i< len(fruits):
#     print(fruits[i])
    # i+=1

# matrix = [[1,2,3],[4,5,6],[7,9,10]]
# for subsets in matrix: 
#     for elements in subsets:
#         print(elements)
#     print(subsets)

# print(matrix[2][0])

# print(type(matrix))


# range function
# numbers = list(range(1,11))
# pop method
# print(numbers.pop())
# print(numbers)

# index method        2nd is for where to start
# print(numbers.index(1,7,11)) # and last one is for where to stop
            #what value 

numbers = [1,2,3,4,5,6,7,8,9,10]
def negative_list(l):
    list1 = []
    for i  in l:
        list1.append(-i)
    return list1
print(negative_list(numbers))










