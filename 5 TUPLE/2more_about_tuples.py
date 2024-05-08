# looping in tuples
# tuple with one element 
# tuple without paraenthesis
# tuple unpacking
# list inside tuple
# some function you can use with tuples 

mixed = (1,2,3,4.0)

# for loop and tuple
# for i in mixed:
#     print(i)
# NOTE we can also use while loop
# i = 0 
# while i in mixed:
#     print(i)
#     i+=1

# tuples with one element
nums = (1,)
words = ('word1',) # if we don't use , comma than tuple is not created
# print(type(nums))
# print(type(words))

# tuple without paranthesis
guitars = 'yamaha','batan rouge','taylor'
print(type(guitars))

# tuple unpacking 
guitarist = ('Maneli jamal', 'Eddie Van Der Meer', 'Andrew Foy')
guitarist1,guitarist2,guitarist3 = (guitarist)
# guitarist1,guitarist2 = (guitarist) these will give error
print(guitarist2)

# list inside tuple
fav = ('southern magnolia',['tokyo ghoul theme','landscape'])
fav[1].pop()
print(fav)
# we can use list inside a tuple
