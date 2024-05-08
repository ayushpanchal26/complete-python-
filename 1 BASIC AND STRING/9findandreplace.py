string = "she is beautiful and she is good dancer"
print(string.replace(" ","_"))
print(string.replace("is","was",1))
#find method
print(string.find("is",1))
# here 1 means that the find operation will work from the 1st index by leaving the other indexes before it
# print(string[28]) #so here we see that find gave the right 
is_pos1 = string.find("is") #pos 1
is_pos2 = string.find("is",is_pos1+1) #so by using these we could find the next is positon
print(is_pos2)

name = input("Enter:")
for i in range(0,1):
    print(name.replace(" ", name[-1::-1]))
    print(name.replace("a", name[1]))

na = "ayushpanchal"
print(na[0:])