# lambda expressions (anonymous function)

def add(a,b):
    return a+b

# lamdas function is used to define a function within a single line of code
add2 = lambda a,b : a+b

# used with built in function like map , reduce , filter 
print(add2(2,3))

sub = lambda a,b : a*b 
print(sub(3,3))

print(sub)
print(add)