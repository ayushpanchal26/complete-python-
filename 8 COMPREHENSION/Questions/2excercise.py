# num to string 
# define a function 

# example 
inp = [True,False,[1,2,3],1,1.0,3]

def integers(l):
    list1  =[]
    for i in l:
        if type(i) == int or type(i) == float:
            list1.append(str(i))
    return list1
# print(integers(inp))


def num_To_str(l):
    return [str(i) for i in l if (type(i) == int or type(i)== float)]

print(num_To_str(inp))