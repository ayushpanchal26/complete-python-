# set comprehension ----->
# set comprehension is rarely used 
s = {k*k for k in range(1,11)}
print(s)

names = ['ayush','dhruvi','khushi']
first = {name[0] for name in names}
print(first)