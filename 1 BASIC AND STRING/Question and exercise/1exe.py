#Ask a user input 3 numbers and you have to print average of three number using string formatting
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))
average = (num1 +num2 + num3)/3
print(f"the average of number{num1},{num2}and{num3} = {average}")
#another method
print(f"Avergae = {(num1+num2 +num3) /3}")