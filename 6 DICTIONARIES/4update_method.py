# update method
user_info = {
    'name': 'ayush', 
    'age': 19,
    'fav_movies':["gang of wassesypur","gow2"],
    'fav_tunes':["azaru","jhak maar ke"],
}

more_info = {'name': 'ayush panchal ','state': 'Rajasthan','hobbies':['coding','reading','guitar']}
# if the other dictionary which is used to update a dictionary has same key then that will get updated
user_info.update(more_info)

print(user_info)

user_info.update({}) # no new data was added to the dictionary 
