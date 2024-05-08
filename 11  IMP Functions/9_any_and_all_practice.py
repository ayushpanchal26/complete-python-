# any all function

def my_sum(*args):
    # args = ()
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        total = 0 
        for num in args:
            total += num
        return total
    return "wrong input"

print(my_sum(12,3,32,32,'ayush'))