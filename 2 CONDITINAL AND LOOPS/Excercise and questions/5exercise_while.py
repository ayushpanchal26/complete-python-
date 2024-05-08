name = input("Enter the name of the person:")
i = 0
temp = ""
while i<len(name):
    if  name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]
    i+= 1