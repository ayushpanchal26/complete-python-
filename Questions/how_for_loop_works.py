# step 1 call iter function
# iter(numbers) ---> iterator 
# next(iter(numbers))
numbers = [1,2,3,4]
number_iter = iter(numbers)
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
# stop iteration
print(next(number_iter))
