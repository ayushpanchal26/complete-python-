# define a function that take a list of strings
# list containing reverse of every string

# NOTE - Use LIST COMPREHENSION 
list1= ['abc','tuv','xyz']

def reverse(l):
    rev = [i[::-1] for i in l]
    return rev

print(reverse(list1))

ev = [i for i in range(1,11) if i%2==0]
print(ev)