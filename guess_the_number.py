import random

def guess():
    x = int(input('Choise the guessing diapazon'))
    computer_choise = random.randint(0, x)
    user_choise = 0
    while user_choise != computer_choise:
        user_choise = int(input(f"Guess the number (0-{x})"))
        if user_choise > computer_choise:
            print('Your number is too high. Try again!')
        elif user_choise < computer_choise:
            print("Your number is too low. Try again!")
    print(f"You got it! The number is {computer_choise}")
guess()