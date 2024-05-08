# tuple data structure
# tuple can store any data type
# Most important tuples are immutable , once tuple is created you can't update data inside tuple
# tuples are faster than lists

example = ('one','two','three')
# no append , no insert, no pop, no remove 

# Methods that can be used in tuple
# count , index 
# len function 
# slicing tuple[]
# print(example[:2])

# tuple with one element ---->> so if we want to create a tuple with one element than it is required that
# with one elemnt we have to use comma ',' after it 
example = (1,) # tuple 
example = (1)  # not tuple 

# tuple without parathesis
snacks = 'puffs','biscuits','chips','chicken tenders' # these is a tuple 
# print(type(snacks))

# tuples unpacking
foods = ('butter chicken','sahi tukda','soyabean')
non_veg,veg,vegan = (foods)
# print(non_veg)
# print(veg)
# print(vegan)


# list inside the list 
fav = ('michigan', ['los angles','USA'])
# now we tuple is immutable but list inside the tuple is mutable
fav[1].pop()
# print(fav)
fav[1].append("UNITED states")
# print(fav)


# max , min ,sum
nums = (1,2,4,5.0)
# print(max(nums))
# print(min(nums))
# print(sum(nums))






def func(int1,int2):
    add = int1+int2
    multiply = int1 * int2
    return add , multiply
    # so when we return 2 or more item than the function will return it in a tuple 


# print(func(2,3))
add , multiply = func(2,3)
# print(add)
# print(multiply)





# more about list , tuple and str

# nums = tuple(range(1,11))
# nums = list((1,2,3,4,5,6,7,8,9,10)) # By using these command we can change tuple to list
nums = str((1,2,3,4,5,6,7,8,9,10))  # changing tuple to string 
nums_list = str([1,2,3,4,5,6,7,8,9,10]) # changing list to string 
print(type(nums_list))

