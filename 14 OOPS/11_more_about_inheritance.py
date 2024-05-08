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
        Phone.__init__(self,brand,model_name,price) # uncommon way to derive  # 1 
        # super().__init__(brand, model_name, price) # 2 
        self.ram = ram 
        self.internal_memory = internal_memory
        self.rear_camera  = rear_camera
     

class FlagshipPhone(Smartphone):
        def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,front_camera):
            super().__init__(brand ,model_name,price,ram,internal_memory,rear_camera)
            self.front_camera  = front_camera


  
smart = Smartphone('redmi', 'Note8Pro', 18000,'6GB', 128, '64 MP')
oneplus  = FlagshipPhone('redmi', 'Note8Pro', 18000,'6GB', 128, '64 MP','12 MP')
# print(oneplus.full_name())
print(smart.full_name())

# print(help.Phone) #help is not working
