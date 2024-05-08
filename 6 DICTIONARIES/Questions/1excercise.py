# define a dictionary containing cube of numbers from 1 to n
def cubefinder(x):
    cubes = {}
    for key in range(0,x+1):
        cubes[key] = key*key*key
    return cubes

n = int(input("Enter:"))
print(cubefinder(n))