#if statment
name = "kashish"
if name == "ayush" or name == "Ayush":
    print("you are ayush")
elif name == "kashish" and  name == "Kashish":
    print("you are kashish")
else:
    print("You are not ayush neither kashish ")
print("..........................................")

'''while loop'''

i = 0
while i<5:
    print(f"ayush:{i}")
    i+=1
print("..........................................")

'''for loop'''

for i in range(1,11,2):
    print(i)

print("..........................................")

'''break and continue'''
for i in range(1,11):
    if i == 5:
        # break
        continue
    print(i)