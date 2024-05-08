# scope of variable
'''there are two types of variable '''
# global and local variable
x = 7
def func():
    global x
    x = 5 # local variable ----> these variable scope is only in these function
    return x
print(x)
print(func())
print(x)