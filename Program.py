import random


def choice_generator():
    computer_choice = random.randrange(1, 4)
    return computer_choice


def winner(pc, cc):
    if pc == cc:
        return 0
    elif ((pc == 1 and cc == 2) or (pc == 2 and cc == 3) or (pc == 3 and cc == 1)):
        return 1
    else:
        return 2


options = {1: "Stone", 2: "Paper", 3: "Scissors"}
results = {0: "IT'S A TIE", 1: "COMPUTER WINS", 2: "PLAYER WINS"}
print('WELCOME TO THE STONE,PAPER,SCISSOR GAME')
print('ENTER YOUR CHOICE : ')
for i, j in options.items():
    print(i, j)

player_choice = int(input())
computer_choice = choice_generator()

print('PLAYER CHOOSES ', options[player_choice])
print('COMPUTER CHOOSES ', options[computer_choice])

w = winner(player_choice, computer_choice)

print(results[w])
