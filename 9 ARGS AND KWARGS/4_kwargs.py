# kwargs(keyword arguments)
# **kwargs(double star operator)


def func(**kwargs):
    for k ,v in kwargs.items():
        print(f"{k} :{v}")

# print(func('achu',first = "ayush" , last = "panchal"))

# dictionary unpacking 
d = {'name':'ayush','age':24}
print(func(**d))
