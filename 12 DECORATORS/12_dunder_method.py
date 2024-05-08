# dunder method
# there are two dunder metod  =  str , repr 
class Phone:
    def __init__(self , brand , model ,price):
        self.brand = brand
        self.model = model
        self.price = price


    def phone_name(self):
        return f"{self.brand} {self.model}"
    
    def __str__ (self):
        return f'{self.brand} {self.model}'

    def __repr__(self):
        return f'Phone(\'{self.brand}\',\'{self.model}\',\'{self.price}\')'

    def __len__(self):
        return len(self.phone_name())

    def __mul__(self, other):
        return self.price * other.price
        

class SmartPhone(Phone):
    def __init__(self, brand, model, price,camera):
        super().__init__(brand, model, price)
        self.camera = camera

    def phone_name(self):
        return f'{self.brand}{self.model}{self.price}'
     
    def __len__(self):
        return self.price 

mob = Phone('mi ', 'asa',42342334)

my_phone  = Phone('redmi' ,'note 8 Pro ',18000)
my_phone2  = Phone('redmi' ,'note 6 Pro ',12000)
my_smarty   = SmartPhone('redmi' ,'note 12 Pro ',25000,'108 MP')
# print(str(my_phone))
# print(repr(my_phone))
# print(my_phone.__repr__())
# print(my_phone * my_phone2)
print(my_smarty.phone_name())
print(len(my_smarty))

# Polymorphism
# having many forms in one is called Polymorphism 
# example :- len function , + etc