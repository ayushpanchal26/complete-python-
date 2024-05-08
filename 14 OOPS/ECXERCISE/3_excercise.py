class Person:
    instance = 0 
    def __init__(self,first_name, last_name , age ):
        Person.instance +=1
        self.first_name = first_name 
        self.last_name = last_name
        self.age = age

    


p1  = Person('Ayush', 'Panchal', 19)
p1  = Person('Santosh', 'Pancahl', 40)
p1  = Person('Santosh', 'Pancahl', 40)
p1  = Person('Santosh', 'Pancahl', 40)
print(Person.instance)