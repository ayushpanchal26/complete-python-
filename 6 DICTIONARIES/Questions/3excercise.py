users = {}

users['name']= input("Enter your name")
users['age'] = int(input("Enter your age:"))
users['favmovies'] = input("Enter movies").split(',')
users['favsongs'] = input("Enter songs").split(',')
# print(users)
for key , value in users.items():
    print(f"{key} :{value}")
