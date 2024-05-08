# def big(a,b,c):
#     if a>b and a >c:
#         return "a"
#     elif b>a and b>c:
#         return "b"
#     return "c"
# print(big(121, 11, 3))
# function inside a functin

# def greates(a,b):
#     if a>b:
#         return a
#     return b

# def new_greatest(a,b,c):
#     # bigger = greates(a, b)
#     return greates(greates(a, b), c)

# print(new_greatest(12, 41, 777))
# palindrome
# def palindrome(word):
#     # for i in range(len(word)):
#         rev = word[-1::-1]
#         if rev == word:
#             return True
#         return False
# print(palindrome("ayush"))















# def ffff(n):
#     a = 0
#     b = 1
#     if n ==0:
#         return a
#     elif n == 1:
#         return b
#     else:
#         for i in range(n-2):
#             c = a+b
#             a = b
#             b = c
#             print(b,end=" ")




# n = int(input())
# print(ffff(n))



















# default paramters



def user_info(first_name , last_name , age = 24):
    print(f"your first name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")
print(user_info("ayush", "panchal", 19))




# scope 







