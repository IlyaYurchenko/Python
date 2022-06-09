from doctest import ELLIPSIS_MARKER
import random
actions = ['rock', 'paper', 'scissors']
user_choise = input('Hi! My name is Lary.\n What is your choise: rock, paper or scissors? \n If you want to stop - write "stop"\n ')
computer_choise = random.choice(actions)
if user_choise == computer_choise:
    print("You have a draw")
elif user_choise == 'rock':
    if computer_choise == 'paper':
        print('Lary wins')
    elif computer_choise == 'scissors':
        print('You win!')
elif user_choise == 'paper':
    if computer_choise == 'scissors':
        print('Lary wins')
    elif computer_choise == 'rock':
        print("You win!")
elif user_choise == 'scissors':
    if computer_choise == 'rock':
        print('Lary wins')
    elif computer_choise == 'paper':
        print('You win!')
else:
    print("error")