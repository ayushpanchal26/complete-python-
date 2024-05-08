#sum of n natural number
#ask a user for natural number(n)
#print total from 1 to n 

n = input("Enter the number:")
n = int(n)

sum = 0
i = 1
while i<=n:
    sum += i
    i+= 1

print(f"Total from 1 to {n} natural number : {sum}")