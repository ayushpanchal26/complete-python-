# in keywords and iteration in dictionary
user_info = {
    'name': 'ayush', 
    'age': 19,
    'fav_movies':["gang of wassesypur","gow2"],
    'fav_tunes':["azaru","jhak maar ke"],
}

# check if key exist in dictionary
# if 'fav_movies' in user_info:
#     print(user_info['fav_movies'])
#     print('present')
# elif 'name' in user_info:
#     print(user_info['name'])
# else:
#     print('not present')

# check if any particular value is in dictionary or not

# ---> values method
# if 19 in user_info.values():
#     print('present')

# if want to check complete list
# if ["gang of wassesypur","gow2"]in user_info.values():
#     print("present")

# loops in dictionaries

# for i in user_info:
#     print(i)
# for i in user_info.values():
#     print(i)


# values method 
# user_info_values = user_info.values()
# print(user_info_values)
# print(type(user_info_values))

# keys method
# user_info_keys = user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))

# how to print values without using values
# for i in user_info:
#     print(user_info[i])

# items method ---> most important
user_items = user_info.items()
print(user_items)
print(type(user_items))

# for i,j in user_info.items():
#     print(f"keys is {i} and values is {j}")


# for i in user_info.items():
#         print(i)