# any , all function

numbers1 = [2,4,6,9,10]
numbers2 = [1,2,3,4,5,6]
evens1 =[]
for num in numbers1:
    evens1.append(num%2==0)

print(evens1)
# print(all([True, True, True, True, True]))

print(any([num%2==0 for num in numbers1]))
print(all([num%2==0 for num in numbers1]))

# any function checks whether any of the value is True or not
# all function checks whether all of the values is True or not 
