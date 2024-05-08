def func(l ,**kwargs):
    if kwargs.get('rev') == True:
        return[i[::-1].title() for i in l]
    else:
        return [i.title() for i in l]

l = ['ayush','panchal','santosh','ravindra']
print(func(l))