# define a function that take list of words as argument and 
# return list with reverse of every element in that list

# examole
# ['abc','tuv','xyz'] --->['cba','vut','zyx']
'''
n = int(input("Enter the size:"))
list1 = []
for i in range(0,n):
    word = input("Enter the word:")
    list1.append(word)

print(list1)

def reverse_of_words(l):
    rev = []
    rev2 = []
    for i in range(len(l)):
        rev.append(list1.pop())

    return rev2
print(reverse_of_words(list1))
'''

# what actully we have to do is here
n = int(input("Enter the size:"))
li = []
for i in range(0,n):
    words = input("Enter the words")
    li.append(words)

print(li)

def reverse_elements(l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements
print(reverse_elements(li))
