def greater(a,b):
    if a>b:
        return a
    return b

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    
def new_greatest(a,b,c):
    # bigger = greater(a, b) #but these is also correct way it is to memorize it
    # return greater(bigger,c)
    return greater(greater(a,b),c) #we can also write it like these 


print(new_greatest(1222,2222,23))

'''Programming Principle  KISS = keep it simple studpid'''