# function with all parameters 
# very imporatant to understand

# PADK ---> paramters -> args -> default paramters -> kwarg

# paramters
# args
# default paramters
# kwargs

def func(name , *args,last_name = 'unkown',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func('ayushpanchal',1,2,3,4,)

    