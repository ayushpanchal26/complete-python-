# OBJECTIVES
# WHAT IS CLASS
# HOW TO CREATE AN CLASS
# WHAT IS INIT METHOD or we can call it  constructor 
# WHAT ARE ATTRIBUTES, INSTANCE VARIABLES
# HOW TO CREATE OUR OBJECT

# NOTE:- In class any function is defined it is called method.

class Person: # according to convention class first letter should be kept capital
    def __init__(self,first_name , last_name , age): # self represnts object  , we can write anything at place of self but according to convention we should write self only
        # instace variables declare
        print('init method // constructor get called')
        self.first_name = first_name 
        self.last_name = last_name
        self.age  = age


# p1 = Person('Ayush','Panchal', 19)
p2  = Person('Santosh','Panchal',40 )

# print(p1.first_name)
print(p2.first_name,p2.last_name,p2.age)