# def is_even(a):
#     return a%2==0
# print(is_even(2))

# is_evens = lambda a : a%2==0
# print(is_evens(8))


# def last_char(s):
#     return s[-1]

# last = lambda s: s[-1]
# print(last('ayush'))


# lambda with if , else
def func(s):
    return len(s)>5

print(func('ayush'))

funct = lambda s :True if len(s)> 5 else False
func3 = lambda s : len(s)>5
print(func3('ayush'))
