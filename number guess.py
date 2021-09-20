import random

print("Welcome to Number Guess game! You have 3 attempts to guess the number right. Options of ranges: 20, 60, or 100")

mode = int(input("Please choose the mode (20, 40, or 60): "))

while (mode != 20) and (mode != 60) and (mode != 100):
    mode = int(input("Please choose the mode (20, 60, or 100): "))

number = random.randint(0, mode)
status = False
attempts = 0

while not status:

    print(f"\n Remaining attempts: {3 - attempts}\n")

    if attempts == 3:
        print("You lost!")
        print(f"The number is {number}")
        break

    if number > (mode / 2):
        if (attempts == 2) and (number >= mode / 2 + mode / 4):
            print(f"The number is more than or equal to {round(mode / 2 + mode / 4)}\n")

        elif (attempts == 2) and (number < mode / 2 + mode / 4):
            print(f"The number is more than {round(mode / 2)} but less than {round(mode / 2 + mode / 4)}\n")

        else:
            print(f"The number is more than {round(mode / 2)}\n")

    if number <= (mode / 2):
        if (attempts == 2) and (number <= mode / 4):
            print(f"The number is less than or equal to {round(mode / 4)}\n")

        elif (attempts == 2) and (number >= mode / 4):
            print(f"The number is more than or equal to {round(mode / 4)}\n")

        else:
            print(f"The number is less than or equal to {round(mode / 2)}\n")

    guess = input("What is the number? ")

    if int(guess) == number:
        print("Yay! You won!")
        status = True

    elif int(guess) != number:
        print("\nThe guess is wrong")
        attempts += 1

    if (not status) and (attempts != 3):
        if number % 2 == 0:
            print("The number is even")
        elif number % 2 != 0:
            print("The number is odd")

