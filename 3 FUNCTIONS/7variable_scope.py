#scope 
x = 5 #global variable 
def func():
    global x
    x = 7  #local variable 
    return x

def func2():
    print(x)

print(func()) #x value will here will only change when the function is called

print(x)