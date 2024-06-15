print("Welcome to my quiz game")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    print("Sorry to see you go, goodbye!")
    quit()

print("Okay! Lets play :)")

score = 0

answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ").lower()

if answer == "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does HDD stand for? ").lower()

if answer == "hard disk drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does SSD stand for? ").lower()

if answer == "solid state drive":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

print("You got " + str(score) + " out of 4")
print("You got " + str((score / 4) * 100) + "%")

