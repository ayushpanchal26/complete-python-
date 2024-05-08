# last excercise
# function
# [1,2,3,[1,2]] ,input and if input [1,2,3,[1,2]]
# output = 1           so output =  2


the_list = [1,2,3,[4,5],[6,7],8,9,[10,11]]

def get_the_correct(l):
    count = 0
    for i in l:
        if type(i)== list:
            count+=1
        else:
            pass
    return count


print(get_the_correct(the_list)) 