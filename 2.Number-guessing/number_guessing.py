import random

max_range = input("Enter max-range of random number: ")

if max_range.isdigit():
    max_range = int(max_range)
    if max_range <= 0:
        print("Please enter a number greater than zero!!!")
        quit()
    else:
        print("Let the game begin!!!")
else:
    print("Incorrect input!")
    quit()


random_num = random.randint(0, max_range)
# print(random_num)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == random_num :
            print("You won!!!")
            print("You got it in", guesses, "guesse(s)")
            break
        elif user_guess > random_num:
            print("Go lower.")
        else:
            print("Go higher")
            
    else:
        print("Please enter a number next time!")
        continue
