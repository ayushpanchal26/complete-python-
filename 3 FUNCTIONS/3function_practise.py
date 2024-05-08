#fuction practise
def last_char(name):
    return name[-1]

print(last_char("ayush kachu"))

# def odd_even(num):
#     if num%2 == 0:
#         # print("number even")
#         return "Even" #we can also return these way also
#     else:
#         return "Odd"
'''odd even '''   
def odd_even(num):
    if num%2 == 0:
        return "Even"
    return "Odd"
print(odd_even(7))

# def is_even(num):
#     if num%2 == 0:
#         return True
#     return False
# print(is_even(5))

'''shortes way to implemet a function pythonic way'''
def is_even(num): #when function is made a that time these value is called parameters
    return num%2==0

print(is_even(10)) #when function is called that time the passed value is called argument

'''no input function'''
def song():
    return "Happy birthday song"

print(song())
