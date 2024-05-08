fruits1 = ['mango','orange']

'''Insert'''
# fruits1.insert(0, 'grapes')
# print(fruits1)
# fruits1.insert(13, 'asdf') 
# print(fruits1)
fruits2 = ['grapes','apple']

'''concatenate'''
# fruits = fruits1+fruits2 
# print(fruits)
# fruits.append('banana')
# print(fruits)

fruits1.extend(fruits2) 
# fruits1.append(fruits2) #list inside the list 
print(fruits1)
print(fruits2)