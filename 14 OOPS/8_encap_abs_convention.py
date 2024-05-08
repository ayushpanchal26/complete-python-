# ABSTRACTION:-  Hiding complexity from the user is known as Abstraction
# Jab tak ENCAPTULATION nhi hoga tab tak ABSTRACTION nhi hoga
# In Python everything is Public nothing is Private


# name manglin 

class Phone:
    def __init__(self, brand , model_name , price):
        self.brand  = brand 
        self.model_name = model_name
        self.__price = price

    def make_a_call(self , phone_number):
        print(f"calling {phone_number}")

    def full_name(self):
        return f"{self.brand} {self.model_name}"
    
    def send_message(self):
        pass # twilio 

# _name is convention for private name 
# __name__  # dunder method  / magic method




phone1 = Phone('redmi ', 'note 8 proo', 18000)
# phone1._price = -1000
print(phone1._Phone__price)
phone1._Phone__price = 17000
print(phone1.__dict__)
# __name  = not a convention . even these is not private but it changes name 
# ex  = __name = _className__name 
# ex = __price will become _Phone__price



l = [3,4,1,2]
l.sort() # tim sort 
# print(l)