l = [1,2,3]

def powers(num, *args):
    if args:
        return [i**num for i in args]
    else:
        print("you didn't pass any args")

print(powers(3,*l))