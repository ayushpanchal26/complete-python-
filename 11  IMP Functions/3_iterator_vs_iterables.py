# iterator vs iterables

numbers = [1,2,3,4] # iterables 
sqaures  = map(lambda a:a*a, numbers) # iterator 
print(sqaures)


print(next(sqaures))