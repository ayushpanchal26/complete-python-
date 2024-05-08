def multiply(*args):
    product = 1 
    print(args)
    for i in args:
        product *= i 
    return product
nums = [2,3,4,5]
print(multiply(*nums))
# by using "*" for any list we can unpack the elements inside the list 
