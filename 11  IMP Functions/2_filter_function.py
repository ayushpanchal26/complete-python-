# filter function 

def is_even(a):
    return a%2==0 

numbers = [3,4,5,6,9,10,2,1]
# evens =[]

evens = tuple(filter(lambda a:a%2==0, numbers))
# for i in numbers:
#     evens.append(is_even(numbers))
print(evens)

for i in evens:
    print(i)

evens2 = [i  for i in numbers if i%2 == 0 ]
print(list(evens))
print(evens2)
# filter function can only be one time iterable 
