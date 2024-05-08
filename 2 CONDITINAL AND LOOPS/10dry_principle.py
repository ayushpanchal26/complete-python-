# winning_number = 26
# guess = 1
# number = int(input("Enter a numbe between 1 to 100:"))
# game_over = False

# while not game_over:
#     if number == winning_number:
#         print(f"you won the games in {guess} times")
#         game_over = True
#     else:
#         if number< winning_number:
#             print("too low")
#         else:
#             print(" to high")

# # dry principle is the best way to do not repeat the code lines 
#         guess+=1
#         number = int(input("Enter a lower number these time"))
'''we can also add the input lines inside the code and if we don't want to use the game_over we can 
        do that thing also'''

winning_number = 26
guess = 1
game_over = False

while True:
    number = int(input("Enter a numbe between 1 to 100:"))

    if number == winning_number:
        print(f"you won the games in {guess} times")
        break

    else:
        if number< winning_number:
            print("too low")
        else:
            print(" to high")

# dry principle is the best way to do not repeat the code lines 
        guess+=1
        continue