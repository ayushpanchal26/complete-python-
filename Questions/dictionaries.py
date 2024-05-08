# Dictionaries
# Q what are dictionaries?
# Unordered collections of any data in key : value pair 

# why we use dictionaries
# Because of limitations of lists, lists are not enough to represent real data.

# Examples
user = {'name':'Ayush','age': 19}
# print(user)

# second method to create dictonary 
user1 = dict(name = 'ayush',age = 19)
# print(user1)

# How to access data from dictionary 
# NOTE----->> There is no indexing because of unordered collection of data.
# print(user['age'])

# which type of data can be stored in dictionary
# anything

# print(user_info['fav_movies'])




# how to add to empty dictionaries
user_info2 = {}
user_info2['name'] = 'ayush'
user_info2['age'] = 19
# print(user_info2)



user_info = {
        'name':'ayush',
        'age': 19,
        'fav_movies':['coco', 'kimi no na wa'],
        'fav_tunes' :['awakening','fairy tale']
}


# check if key exist in dictionary 
# if 'names' in user_info:
#     print("available")
# else:
#     print('not present')

# check if value exist in dictionary
# if 19 in user_info.values():
#     print("available")
# else:
#     print('not present')

# loops in dictionaries
# for i in user_info.values():
    # print(i)

user_key = user_info.keys()  # it stores all the key of any dictonary
user_value = user_info.values() # it stores all the values of any dictonary
# print(user_key)
# print(type(user_key))
# print(type(user_value))

# items method 
user_items = user_info.items()
# print(user_items)
# print(type(user_items))

# why item method is useful------->

# for key, value in user_info.items():
#     print(f"key is {key} and value is {value}")


ayush ={
    'full name' :'ayush panchal',
    'age': 19,
    'staus':'depressed',
}

# for key, value in ayush.items():
#      if 19 in ayush.values():  
#         print(f"These are:{key}:These are {value}")

# how to add data in dictionaries
user_info = {
        'name':'ayush',
        'age': 19,
        'fav_movies':['coco', 'kimi no na wa'],
        'fav_tunes' :['awakening','fairy tale']
}

user_info['fav_songs'] = ['song1','song2']

# pop method
# popped_item = user_info.pop('fav_tunes')    
# print(f"popped item is {popped_item}")
# print(user_info)


# popitem() method 
popped_item = user_info.popitem()
print(type(popped_item))
print(user_info)