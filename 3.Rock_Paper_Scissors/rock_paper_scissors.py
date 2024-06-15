import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter rock/paper/scissors or q to quit: ").lower()

    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    if user_input == "rock":
        user = 0
    elif user_input == "paper":
        user = 1
    else:
        user = 2
    
    rand_num = random.randint(0, 2)

    # #rock: 0, paper: 1, scissors: 2
    computer_pick = options[rand_num]

    print("Computer picked", computer_pick +"." )

    # print(rand_num)
    if user == rand_num:
        print("Draw!!!")
        continue    
    elif (user == 0 and rand_num == 2) or (user == 1 and rand_num == 0) or (user == 2 and rand_num == 1):
        print("You win!!!")
        user_wins += 1
        continue
    else:
        print("Computer wins!!!")
        computer_wins += 1
        continue


if computer_wins > user_wins:
    print("Computer won with best score of", computer_wins, "and you had", user_wins)
elif computer_wins < user_wins:
    print("You won with best score of", user_wins, "and computer had", computer_wins)
else:
    print("It is a tie.")

print("Thanks for playing, goodbye...")




    # if user_input == "rock" and computer_pick == "scissors":
    #     print("You won!!!")
    #     user_wins += 1
    #     continue

    # elif user_input == "paper" and computer_pick == "rock":
    #     print("You win!!!")
    #     user_wins += 1
    #     continue
    
