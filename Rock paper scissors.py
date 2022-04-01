import random

def play():
    user = input("What do you choose? 'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It\s a tie"

    if is_win(user, computer):
        return "you won rock paper scissors!!"

    return "you lost rock paper scissors ;("

def is_win(player1, player2):
    if (player1 == 'r' and player2 == 's') or (player1 == 's' and player2 == 'p') or (player1 == 'p'and player2 == 'r'): 
        return True

print(play())

