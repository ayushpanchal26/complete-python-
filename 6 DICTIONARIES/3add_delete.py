# add and delete data 
user_info = {
    'name': 'ayush', 
    'age': 19,
    'fav_movies':["gang of wassesypur","gow2"],
    'fav_tunes':["azaru","jhak maar ke"],
}

# how to add data
# user_info['fav_songs'] = ['song1', 'song2']
# print(user_info)

# pop method  ---> its data type depend on the value which will get returned
# popped_item = user_info.pop('fav_tunes')
# print(f"popped item = {popped_item}")
# print(user_info) 

# popitem method --> these method delete the key value pair from the list by iteself 
# it return the tuple value 
popped_item = user_info.popitem()
print(user_info)
print(popped_item)
print(type(popped_item))
# user_info.popitem()
# user_info.popitem()
# user_info.popitem()
print(user_info)