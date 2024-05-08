fruits = ['grapes', 'mango ', 'apple']
fruits.sort()
print(fruits)
fruits2  = ('grapes','mango','apple')
print(sorted(fruits2))
fruits2  = {'grapes','mango','apple'}
print(sorted(fruits2))

guitars = [
    {'model':'yamha file','price':8400},
    {'model':'failtj naptune','price':50000},
    {'model':'faith apollo venus','price':35000},
    {'model':'taylor 814ce','price':450000},
]

print(sorted(guitars,key =  lambda d :d['price'], reverse = True))