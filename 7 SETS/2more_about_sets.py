# in keyword in sets and for loop
# set is used to remove duplicates

s = {'a','b','c'} # set don't have any order it is unordered 

# in keyword to check if item is present or not in set 
if 'a' in s:
    print('present')
else:
    print('not present')

# for loop
for items in s:
    print(items)

# union 
s1 = {1,2,3,4}
s2 = {3,4,5,6}
union_set = s1 | s2   
# '|' these symol is known as pipe 
# print(union_set)
print(s1 & s2)