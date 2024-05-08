fruits =['mango', 'orange','apple']
fruits2 = ['watermelon','grapes']
# what is differnce between append and extend method
# fruits.append(fruits2)
# print(fruits)
# fruits.extend(fruits2)
# print(fruits)
'''
append method is used to add the whole list to the another list
extend method adds the elements of one list to another list 
'''
# sort method is used in list to sort the elements inside the list in alphabetic manner or numbers manner 

fruits.sort()
print(fruits)


f1 = ['orange','apple','pear']
f2 = ['banana','kiwi','apple','banana']
print(f1 is f2) # is check whether the address is same or not
print(f1 == f2) # == check whether the list or any vairables values are same or not
