# define a genrator function
# take one number as argument 
# generate a sequence of even numbers from 1 to that number

def even(a):
    for i in range(1,a+1):
        if i%2==0:
            yield i

def even2(n): # dry principle
    for i in range(2,2+1,2):
        yield i 


for num in even(7):
    print(num)