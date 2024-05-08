# *args with normal paramters

def multiply(num1,num2,*args):
    product = 1
    print(num1, num2)
    print(args)
    for i in args:
        product *= i
    return product
print(multiply(2,3))

