# make flexible functions

# *operator 
# *args

# args is not a keyword

# def total(a,b):
#     return a+b

# print(total(3, 4))

def all_total(*args):
    totals = 0
    for nums in args:
        totals += nums
    return totals

print(all_total(1,2,3,4,5))