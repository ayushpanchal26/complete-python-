# Decorators - enhance the functionality of other functions
# @ use for decorator


def decorator_function(any_func):
    def wrapper_function():
        print('this is awesome function')
        any_func()
    return wrapper_function()

@decorator_function
def func():
    print('this is function 1')

var  = func()
print(var)
def func2():
    print('this is function 2')

# func1 = decorator_function(func1)
