import math
import random

def play (the_guess, the_secret, choices):
    if the_guess == the_secret:
        print("\nCorrect! The secret number was " + str(the_secret))
        hint = ""
    else:
        hint = ""
        choice = random.randint(1, 6)
        while choice in choices:
            choice = random.randint(1, 6)
        if choice == 1:
            hint = "Hint: your number is "
            if math.isclose(the_guess, the_secret, rel_tol = 0.1):
                hint += "close!"
            else:
                hint += "not close!"
            choices.append(choice)
        elif choice == 2:
            hint = "Hint: your number is a factor of " + str(the_secret*random.randint(3, 9))
            choices.append(choice)
        elif choice == 3:
            hint = "Hint: the secret number is "
            if the_secret < the_guess:
                hint += "lower than your guess"
            else:
                hint += "higher than your guess"
            choices.append(choice)
        elif choice == 4:
            hint = "Hint: your number is divisible by "
            x = math.ceil(the_secret/2)
            while the_secret % x != 0:
                x -= 1
            hint += str(x)
            if x == 1:
                hint = "Hint: your number is prime"
            choices.append(choice)
        elif choice == 5:
            closeNum = the_secret + random.randint(-10, 10)
            hint = "Hint: your number is close to " + str(closeNum)
            choices.append(choice)
        elif choice == 6:
            hint = "Hint: your number is "
            if the_secret % 2 == 0:
                hint += "even"
            else:
                hint += "odd"
            choices.append(choice)
        if hint != "":
            print ('\n' + hint)
        if the_guess != the_secret:
            the_guess = int(input("\nEnter new guess: "))
        if len(choices) < 6:
            play(the_guess, the_secret, choices)
            return
        if len(choices) >= 6:
            print("\n\n\n\n\n\n*****************************")
            print("Out of lives! The secret number was: " + str(the_secret))
            print("*****************************")


choice_list = []
print("\nWelcome to the number guessing game! You have 7 lives and will get a hint after every wrong answer.\n")
play_again = "y"
while play_again == "y":
    range = int(input("Please input the max value for the range of numbers starting at 1: "))
    secret_num = random.randint(1, range)
    guess = int(input("Enter your guess: "))
    has_printed = False
    play(guess, secret_num, choice_list)
    play_again = input("\n\n\n\n Would you like to play again? Input y/n: ")