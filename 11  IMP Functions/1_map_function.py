# map function

numbers = [1,2,3,4]

def square(a):
    return a*a 

squares = list(map(lambda a: a**2,numbers))
print(squares)

# # list comp
# squaress  = [i**2 for i in numbers]
# print(squaress)

# new = []
# for i in numbers:
#      new.append(square(i))

# print(new)


names = ['abc','abcd','abcde']


length  =  map(len,names)

for i in length:
    print(i)
for j in length:
    print(j)
# we can only loop MAP function only one time until it is not converted in any other data type 
# MAP object is an iterator 
