class Phone:
    def __init__(self , brand , model_name , price):
        self.brand = brand
        self.model_name = model_name
        self._price  = price

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self,number):
        return f"calling {number}......"
    

class Smartphone(Phone): # derived / child class
    def __init__(self , brand , model_name , price, ram , internal_memory , rear_camera):
        # two ways to use base class
        # Phone.__init__(self,brand,model_name,price) # uncommon way to derive  # 1 
        super().__init__(brand, model_name, price) # 2 
        self.ram = ram 
        self.internal_memory = internal_memory
        self.rear_camera  = rear_camera
     
    def full_seps(self):
        return f"Compny -  {self.brand} \n model - {self.model_name} ]n Price - {self._price} \n Ram - {self.ram} \n Memory - {self.internal_memory}  \n Camer - {self.rear_camera}"

phone = Phone('nokia', '1100',1000)
smartphone = Smartphone('oneplus','5', 30000,'6 GB', '64 GB','20 MP')
print(phone.full_name())
print(smartphone.full_name())
print(smartphone.full_seps())