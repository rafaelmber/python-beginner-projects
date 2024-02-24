import random

options = ['r', 'p', 's']

def play():
    print('Welcome to Rock, Paper, Scissors. Select an option')
    user = input("'R' for Rock, 'P' for Paper, and 'S' for Scissors: ").lower()
    computer_option = random.choice(options)

    print(f'Computer choose {computer_option}')

    if(user == computer_option):
        return "It's a tie"
    
    if is_win(user, computer_option):
        return "You Won"
    else:
        return "You lose"
    

def is_win(player, opponent):
    # Returns True if the player wins
    if((player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p')):
        return True

if __name__ == '__main__':
    print(play())