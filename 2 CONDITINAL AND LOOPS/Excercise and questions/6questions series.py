''' first 10 odd , even , natural and whole numbers '''
# i = 0 
# while i<=10:
#     if(i%2== 0):
#         print(f"{i} is a Even number")
#     elif(i%2 != 0):
#         print((f"{i} is a Odd number"))
#     else:
#         print(i)

#     i+=1
# n = 0 
# print("whole and natural")
# while n<=10:
#     if(n!=0):
#         print(f"{n} are Natural number")
#     else:
#         print(f"{n} these is whole number")
#     n+=1

'''first 10 natural number and their squares '''
i = 1
while i<=10:
    print(f" Square of {i} = {i*i}")
    i+=1

'''loop statemene to print to 10,20,30 upto 300'''
i = 10 
while i<=300:
    print(f"{i}")
    i+=10

'''while loop  staement to print 105,98,91 upto 7'''
i = 105
while i>=7:
    print(f"series = {i}")
    i-=7

'''print  sum of first 10 natural numbers'''
n = 0
sum = 0 
while n<=10:
    sum = sum + n
    n+=1
print(f"sum of 10 natural number = {sum}")


'''sum of first 10 even numbers'''
y = 0
sum = 0 
while y<=10:
    if(y%2 == 0):
        sum+=y
    y+=1
print(f"sum of first 10 even number = {sum}")

print(2+4+6+8+10)

'''print table of the number entered by the user'''
num = int(input("Enter the number"))
i = 1
while i<=10:
    print(f"{num} x {i} = {num*i}")
    i+= 1
'''print all even numbers that falls bw the numbers that user enters'''
# num1= int(input("Enter the number"))
# num2 = int(input("Enter the number 2"))
# if num1>num2:  
#     while(num1>num2):
#         if num2%2==0:
#             print(num2)
#         num2+=1
# else:
#     while(num2>num1):
#         if num1%2 == 0:
#             print(num1)
#         num1+=1

'''prime number -- not did '''
# num = int(input("Enter"))

# i = 2
# while i<num:
#     if (num %i ==0):
#         False
#     else:
#         print(f"{num} is Prime number")
#     i+=1
'''reverse the number -20%'''
r = 0 
rnum = 0
i = 0 
num1 = int(input("enter"))
while num1 != 0:
    r = num1 %10 
    rnum = rnum *10 +r
    num1 = num1//10
    i+=1
print(rnum)

