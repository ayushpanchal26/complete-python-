# instance method 
class Person:
    def __init__(self,first_name , last_name,age):
        self.first_name  =  first_name
        self.last_name = last_name
        self.age = age
    def full_name(self):
        return f"{self.first_name} {self.last_name} and Age is {self.age}"

    def is_above_18(self):
        return self.age>18

p1 = Person('Ayush', 'Panchal',19)
# print(p1.full_name())
p2 = Person('Santosh', 'Pancahl', 40)
# print(p2.full_name())
# print(Person.full_name(p2)) # another syntax
print(Person.is_above_18(p1))

# type of syntax

l = [1,2,3]
list.clear(l)
# print(l)