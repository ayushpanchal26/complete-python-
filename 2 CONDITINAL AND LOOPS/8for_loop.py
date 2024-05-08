'''basic syntax
for i in range(1,11):
    print(f"hi : {i}")
    '''
# total = 0
# for i in range(1,11):
#     total+=i
# print(f"{total} is the add")

# n = int(input("Enter:"))
# sum = 0
# for i in range(1,n+1):
#     sum+= i
# print(f"{sum} is the total of number from n")

# n = input("Enter:")
# n_len = len(n)
# sum = 0 
# for i in range(0,n_len):
#     sum += int(n[i])
# print(sum)

name = input("Enter your name")
temp = ""
for i in range(0,len(name)):
     if name[i] not in temp:
        print(f"{name[i]}:{name.count(name[i])}")
        temp+=name[i]
     i+=1
