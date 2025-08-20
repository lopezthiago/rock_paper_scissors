import random

name = input('Name? ').title()
computer_score = 0
user_score = 0

def score():
    return (f'{name} score: {user_score} Computer score: {computer_score}')

def user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in [f'rock', 'paper', 'scissors', 'r', 'p', 's']:
        choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    mapping = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    return mapping.get(choice, choice)

def computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def winner(user, computer, user_score, computer_score):
    if user == computer:
        print('Its a Tie!')

    elif (user == 'rock' and computer == 'scissors') or \
        (user == 'paper' and computer == 'rock') or \
        (user == 'scissors' and computer == 'paper'):
        print(f'{name} Wins!')
        user_score += 1
    else:
        print('Computer wins!')
        computer_score += 1
    return user_score, computer_score

while True:
    user_score, computer_score = winner(user_choice(), computer_choice(), user_score, computer_score)
    print(score())
    again = input('Again? y/n ')
    if again == 'y':
        continue
    elif again == 'n':
        break
    else:
        input('Invalid input. Please enter y or n: ')
        continue
