def add(a,b):
    if (type(a) is int ) and (type(b) is int ):
        return a+b
    raise TypeError('oops ypu are passing wrong data type for a function')

print(add(12,'as'))
