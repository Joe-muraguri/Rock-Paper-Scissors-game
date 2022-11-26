import random
import sys

print("ROCK PAPER SCISSORS")

wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' %(wins,losses,ties))
    
    while True:
        print("Enter your move: (r) for rock, (p) for paper, (s) for scissors and (q) to quit the game")
        playerMove = input()
        
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print("Enter of r, p, s or q")

    if playerMove == 'r':
        print("ROCK VERSES...")
    elif playerMove == 'p':
        print("PAPER VERSES ...")
    elif playerMove == 's':
        print("SCISSORS VERSES...")
    
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print("ROCK")
    if randomNumber == 2:
        computerMove = 'p'
        print("PAPER")
    if randomNumber == 3:
        computerMove = 's'
        print("SCISSORS")

    if playerMove == computerMove:
        print("Its a tie !")
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print("You Win !!")
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print("You Lose!!")
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'p':
        print("You Win !!")
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print("You Win !!")
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'r':
        print("You Lose")
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print("You Lose!!")
        losses = losses + 1


    

