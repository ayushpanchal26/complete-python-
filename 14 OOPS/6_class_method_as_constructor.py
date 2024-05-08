class Person:
    count_instance = 0  # class variable or class attributes
    def __init__(self , first_name , last_name , age):
        Person.count_instance += 1 
        self.first_name =  first_name
        self.last_name = last_name
        self.age = age

    @classmethod  # our own construtor 
    def from_string(cls,string):
        first,last,age  = string.split(',')
        return cls(first,last,age)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"



    @classmethod
    def count_instances(cls): #accourding to convention cls
        return f"you have created {cls.count_instance} instances {cls.__name__} of person class"

 

p1 = Person('Ayush','Panchal', 9)
p2 = Person('Santosh','Panchal',40)
p3 = Person.from_string('ayush,panchal,19')
print(p3.full_name())
print(Person.count_instances())
"you have created 4 isntances of person class"