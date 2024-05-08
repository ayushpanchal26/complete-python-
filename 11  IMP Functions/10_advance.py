# advance min and max 
# numbers = [1,2,4,5,7]
# print(max(numbers))



names = ['ayushpanchal','akhilsharma','akash','A']
# print(min(names,key = lambda item:len(item)))
# print(max(names,key = lambda item:len(item)))

students = {
    'ayush':{'score':12,'age':24},
    'mohit':{'score':75,'age':19},
    'rohit':{'score':76,'age':23}
}

student2 = [
    {'name':'ayush','score':90,'age':24},
    {'name':'mohit','score':70,'age':19},
    {'name':'rohit','score':60,'age':27}
]

print(max(student2, key = lambda item:item.get('age'))['name'])
print(max(students,key= lambda item:students[item]['score']))