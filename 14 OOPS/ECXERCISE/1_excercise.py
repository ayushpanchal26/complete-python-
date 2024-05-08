# create a laptop class with attributes like brand name , model name , price
# create two objects/instance of your laptop class
class Laptop:
    def  __init__(self , laptop_brand , laptop_model, laptop_price):
        self.laptop_brand  = laptop_brand
        self.model_number  =  laptop_model
        self.lapi_price = laptop_price
        self.laptop =  laptop_brand + ' ' +laptop_model

l1 = Laptop('Dell', 'G15', 131000)
l2 = Laptop('Dell', 'Studio', 50000)

print(l1.laptop)