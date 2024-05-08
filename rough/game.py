import random as ra
win = ra.randint(1, 100)
game_over = False
guess= 1
number  = int(input("Enter"))

while not game_over:
    if number == win:
        print(f"you win! and you did it in {guess} times")
        game_over = True
    else:
        if number< win:
            print("to low")
        else:
            print("to high")
    guess += 1
    number  = int(input("Enter again"))
        