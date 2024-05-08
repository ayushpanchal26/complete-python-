def is_greatest(a,b,c):
    if a>b and a>c:
        return "a is greater"
    elif b>a and b>c:
        return "b is greater"
    return "c is greater"

n1 = int(input("Enter number 1:"))
n2 = int(input("Enter number 2:"))
n3 = int(input("Enter number 3:"))
print(is_greatest(n1, n2, n3))
print(is_greatest(12,13,11))
