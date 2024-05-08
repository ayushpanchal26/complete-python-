# tuples
# tuples are immutable
# tuples are ordered collection of items
# tuples can store any data type
# you cannot change (add or delete ) values from tuple once it created
# but can add, data from which is present inside tuples


mixed = (1,2,3,4,5,'six')
# mixed1 = (1,2,3,4,5) #to use sum() function all elements in the tuple should be integers or float
# no append , no pop , no insert , no remove
# only count index

# function 
# min(), max(), len(), sum()

# print(sum(mixed1))
mixed_2 = (1,2,3,4,5,[6,7,8])
mixed_2[5].pop()
print(mixed_2)