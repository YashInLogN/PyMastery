import random

choices = ['rock', 'paper', 'scissor']

print('Welcome to the ROCK, PAPER, SCISSOR Tournament!')

n = int(input("How many rounds: "))
count_computer = 0
count_player = 0
for i in range(n):
    computer_choice = random.choice(choices)

    print(f'Computer: {computer_choice}')

    player_choice = None
    while player_choice not in choices:
        player_choice = input(f'Enter ur choice {choices}: ').lower()

    # if computer_choice == player_choice:
    if computer_choice == 'rock':
        count_computer += 1
    elif computer_choice == 'paper':
        count_player += 1
    elif computer_choice == 'scissor':
        if player_choice == 'rock':
            count_player += 1
        else:
            count_computer += 1
            
    print(f'Computer: {count_computer}, Player: {count_player}')
    print('\n')


if count_player == count_computer:
    print('Tie')
elif count_player > count_computer:
    print('You Win')
else:
    print('Computer Wins')



