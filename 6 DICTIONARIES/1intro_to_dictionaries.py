# dictionaries intro 
#  Q - why we use dictionaries?
#  A - Because of limitations of lists , lists are not enough to represent real data

# example
# user  =[ ['ayush',19]['sanju','gang of wasseypur'],['khakhi', 'mirzapur']]
# this list contains user name , fav movies and series
# you can do this but this is not a good way to do this.

# Que - what are dictionaries
# Ans - unrodered collection of data in key : value pair

# how to create dictionaries
# user = {'name': 'Ayush', 'age': 19}
# print(user)
# print(type(user))

# second method to create dictionary 
# user1 = dict(name = 'ayush',age = 19)
# print(user1)
# print(type(user1))


# how to access data in dictionaries
# print(user['name'])
# print(user['age'])

# which type of data a dictionary can store
#  answer is = anything
# numbers, string , list , dictionaries and we can store every type of data in dictionaries
user_info = {
    'name': 'ayush', 
    'age': 19,
    'fav_movies':["gang of wassesypur","goq2"],
    'fav_tunes':["azaru","jhak maar ke"],

}
print(user_info)
print(user_info['fav_movies'])


# dictionaries inside dictionary
user_inside = {
    'user1': {
         'name': 'ayush', 
    'age': 19,
    'fav_movies':["gang of wassesypur","goq2"],
    'fav_tunes':["azaru","jhak maar ke"],
    },
    'user2': {
          'name':'xyz',
          'age': 21,
          'fav_movies':["gang ","why2"],
          'fav_tunes':["kikiki","kekeke"],
    }
}
print(user_inside['user1'])
print(user_inside['user2'])

# how to add data to empty dictionaries
user_info2 = {}
user_info2['name'] = 'ayush'
user_info2['age'] = 19

print(user_info2)