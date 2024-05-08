user_info = {
        'name':'ayush',
        'age': 19,
        'fav_movies':['coco', 'kimi no na wa'],
        'fav_tunes' :['awakening','fairy tale']
}

more_info ={
    'name':'ayushpanchal',
    'state':'rajasthan',
    'hobbies':['coding','overthinking','gaming']
}
user_info.update(more_info)
# print(user_info)

# from keys 
d = {
    'name': 'unknown',
    'age': 'unkown'
}
d = dict.fromkeys(['name','age','height'],'unkown')
# print(d)
family = dict.fromkeys(('ayush','santosh','ravindra','nency'),'panchal')
# print(family)
example = dict.fromkeys(range(1,11),'unkown')
# print(example)

d1 = dict.fromkeys(['name','age'],['unknown','unknown'])
# print(d1) # the values passed for the keys whether it is 1 or more than 1 it will be same for every keys 


# get method (useful)
dic = {'name':'unknown','age':'unkown'}
# print(dic['names'])  # these will return an error 
# print(dic.get('name')) # these will not give error
# get key gives None result if there is no value found in the dictionary
# if none ----> False(none is evaluated as False) 
# and else is ----> True(else is evaluated as Ture) but for get method 

# dic.clear()
# print(dic)
d112 = {}
d112  = dic.copy()
print(d112)