inp = input("Enter the number ")
lenn = len(inp)
i = 0
total = 0
while i<lenn:
    total = total + int(inp[i])
    i += 1

print(total)