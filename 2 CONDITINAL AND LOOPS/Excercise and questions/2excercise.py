#ask user's name and age
#if user' name start with ('a' or 'A') and age is above 10 then
name = input("Enter your name")
age = int(input("\nEnter your age"))
name_lower = name.lower()

#mine 
if name_lower[0] == 'a' and age >= 10:
    print("you can watch cocomo movie")
else:
    print("you cannot watch cocomo movie")

#legit
if age>=10 and (name[0]=='a' or name[0]== 'A'):
    print("you can watch cocomo movie")
else:
    print("you cannot watch cocomo movie")

    