# Q1
numbers = [1,2,3,4,5,6,7,8,9,10]
def square_list(l):
    square = []
    for i in l:
        square.append(i*i)
    return square
# print(square_list(numbers))

# Q2 
words = ['words1','word2','word3']
def reverse(l):
    rev = []
    for nums in range(len(l)):
        popped = l.pop()
        rev.append(popped)
    return rev
# print(reverse(words))

# Q3
word = ['abc','tuv','xyz']
def reversedd(l):
    revv = []
    for i in l:
        # popp = l.pop()
        revv.append(i[::-1])
    return revv
# print(reversedd(word))

# Q4
numbers = [1,2,3,4,5,6,7]
def filters(l):
    odd = []
    even  = []
    for i in l:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    # output = [even , odd]
    # return output
    return [even , odd]


# print(filters(numbers))

# Q5
num1 = [1,2,5,8]
num2 = [1,2,7,6]
def common(l1,l2):
    commons = []
    for i in l1:
        if i in l2:
            commons.append(i)
    return commons
# print(common(num1, num2))


# print(min(num1))

def greatest_differnce(l):
    diff = max(l) - min(l)
    return diff
# print(greatest_differnce(num1 ))
        
# Q 6
list1 = [ 1,2,3, [1,2],[2,3]]
def check(l):
    counts = 0
    for i in l:
        if type(i) == list:
            counts+= 1
        else:
            pass
    return counts

print(check(list1))
            