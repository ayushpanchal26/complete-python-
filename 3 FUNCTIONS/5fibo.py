# 13650hx
#fibonacci series

# #3 -----> 1 2 3
# for i in range(1,11):
#     print(i,end=" ")
# print("\n")

def fibonacci_seq(n):
    a = 0 #first number
    b = 1 # second number
    if n == 1:
        print(a)
    elif n == 2:
        print(a,b) # a b , 0 1
    else: #i.e user have inputed number bigger than 1
        print(a,b ,end=" ")
        for i in range(n-2):
            c = a+b # here c = 1+0, c = 1+1 , c = 3, c = 5
            a = b # a=1 , a = 1 , a = 2 , a= 3
            b = c # b = 1 , b = 2 , b = 3 , b= 5
            print(b ,end=" ")
    

inp = int(input("Enter"))
print(fibonacci_seq(inp))