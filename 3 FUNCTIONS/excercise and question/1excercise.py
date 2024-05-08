'''write a function to print which number is greater'''

def is_greater(a,b):
    if a>b:
        return f"A is Greater = {a}"
    return f"B  is Greater = {b} "

num1 = int(input("enter "))
num2 = int(input("enter"))
print(is_greater(num1, num2))