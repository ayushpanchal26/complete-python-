# we will discuss three problems in existing 
# then we will solve them using getter, setter decorator 

class Phone:
    def __init__(self, brand , model_name , price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)
        # if price>0:
        #     self._price = price
        # else:
        #     self._price = 0
        # self.completer_specification = f"{self.brand} {self.model_name} and price = {self._price}" # instance variable 
    
    @property
    def completer_specification(self):
        return f"{self.brand} {self.model_name}  and price = {self._price}"
    

    @property # getter 
    def price(self):
        return self._price
    

    @price.setter #setter 
    def price(self,new_price):
        self._price = max(new_price,0) # in real world programs instead of setting values to zero or any default values we 
                              # we raise errors


    def make_a_call(self, phone_number):
        print(f"calling {phone_number}")

    def full_name(self):
        return f"{self.brand} {self.model_name}"


phone1 = Phone('Nokia',"1100", -1000)

phone1.price  = -5000
print(phone1.price)
print(phone1.completer_specification)
