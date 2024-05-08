# Class methods
# Differnce between class methods and instance methods
class Person:
    count_instance = 0  # class variable or class attributes
    def __init__(self , first_name , last_name , age):
        Person.count_instance += 1 
        self.first_name =  first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def count_instances(cls): #accourding to convention cls
        return f"you have created {cls.count_instance} instances {cls.__name__} of person class"

 

p1 = Person('Ayush','Panchal', 9)
p2 = Person('Santosh','Panchal',40)
print(Person.count_instances())
"you have created 4 isntances of person class"