import random
num = int(input("Enter:"))
guess = 1
win = 46
# win = random.randint(1, 100)
for i in range(0,100):
        if num != win :
            num = int(input("Enter again:"))
            if num<win:
                print("too loo")
            elif num>win:
                print("too high")
            elif num>100:
                print("not applicable")
            else:
                print("done for the day")
            
        elif num == win:
            print(f"You won,you guessed the number in {i} times")
            break
        

'''legit way'''
# winning_number = random.randint(1, 100)
winning_number = 26
guess = 1
number = int(input("Enter a numbe between 1 to 100:"))
game_over = False

while not game_over:
    if number == winning_number:
        print(f"you won the games in {guess} times")
        game_over = True
    else:
        if number< winning_number:
            print("too low")
            guess+=1
            number = int(input("Enter a higher number these time:"))
        else:
            print(" to high")
            guess+=1
            number = int(input("Enter a lower number these time"))