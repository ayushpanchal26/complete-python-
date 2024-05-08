# list chapter summary
# list is data structure that can hold any type of data

# create a list
words = ['word1', 'word2']

# you can store anything inside a list
mixed = [1,2,3,[4,5,6],'seven',8.0,None]

# list is ordered collection of items
# print(mixed[0])
# print(mixed[3])

# add data to our list
# append method

# mixed.append('10')
# print(mixed)

# mixed.append([10,20,30])
# print(mixed)

# extend method
# mixed.extend([10,20,30])
# print(mixed)

# join two list
#  l = l1+l2 

# insert method 
# mixed.insert(1,"inserted")
# print(mixed)

# remove the data 
# popped = mixed.pop() # remove the last item
# print(popped)
# print(mixed)

# popped_more = mixed.pop(1) # remove item the from the given postion
# print(popped_more)
# print(mixed)

# remove
# mixed.remove('seven')
# print(mixed)

# del statment 

# del mixed[3]
# print(mixed)

# loop in list

for i in mixed:
    print(i)