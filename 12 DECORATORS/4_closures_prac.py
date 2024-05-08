# function returning function(closure) practice 

def to_power(x):
    def calc_power(n):
        return n**x
    return calc_power


cube = to_power(3)
print(cube(5))

def power(x):
    def calc(n):
        return n**x
    return calc 

square  = power(2)
print(square(9))