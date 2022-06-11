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
# guess()

def computer_guess():
    start = 0
    stop = int(input("Choose the guessong diapazon\n"))
    feedback = ''
    while feedback != 'yes':
        computer_guess = random.randint(start, stop)
        feedback = input(f"is {computer_guess} correct?\n[y]if correct \n[h] if higher than your number \n[l] if lower then your number ").lower()
        if feedback == "h":
            stop = computer_guess - 1
        elif feedback == 'l':
            start = computer_guess + 1
        elif feedback == "y":
            print("Got you!")
            break
        else:
            print("ERROR")
            break

computer_guess()