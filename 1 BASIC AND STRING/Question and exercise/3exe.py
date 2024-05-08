'''
take two comma separated inputs from user
1) user's name,
2) A single character

output - 2 print lines
1) user'name length
2)count the character that user inputed
'''
name,char = input("Enter comma separated name and chracter:").split(",")
case_insestive = name.lower()
char.lower()
print(f"length of your name is = {len(case_insestive)}")
print(case_insestive.count(char))