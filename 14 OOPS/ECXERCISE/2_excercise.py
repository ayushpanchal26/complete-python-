# class Laptop:
#     def __init__(self, brand , model_name , price):
#         self.brand  = brand
#         self.model_name = model_name
#         self.price = price

#     def percentage_off(self,n):
#          discounted_price = (n/100)*self.price
#          return self.price - discounted_price
#     def name(self):
#         self.model_name = 'ayush;s new'
#         return self.model_name



# l1 = Laptop('dell', 'g15', 131000)
# l2 = Laptop('dell', 'studio', 60000)
# print(l2.percentage_off(5))
# print(l1.name())


''' example of class variable'''
class Laptop:
    discount = 10 
    def __init__(self, brand , model_name , price):
        self.brand  = brand
        self.model_name = model_name
        self.price = price

    def percentage_off(self):
         discounted_price = (self.discount/100)*self.price
         return self.price - discounted_price
    def name(self):
        self.model_name = 'ayush;s new'
        return self.model_name



Laptop.discount = 20 
l1 = Laptop('dell', 'g15', 131000)
l2 = Laptop('dell', 'studio', 60000)
print(l2.percentage_off())
l2.discount =  50
print(l2.__dict__)
print(l2.percentage_off())