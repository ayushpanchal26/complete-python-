name = "ayush"
print(name.center(9,"*"))
namein = input("Enter your name")
length = len(namein)
print(name.center(length+4,"*"))

#these is also correct but legit way is 
print(name.center(len(namein)+8,"/"))