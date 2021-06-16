#Rock, Paper, and scissor game

import random

print("Welcome to the Game\n" "Choose Rock(R), Paper(P), or Scissor(S)")
i = 0
x = 0
y = 0
z = 0
while(i<5):
    i = i + 1
    you = input("Type one letter in capital\n" "1. R\n" "2. P\n" "3. S\n")
    comp = random.randint(1,3)


    if comp == 1 and you == 'R':
        print("computer chooses Rock")
        print("Tie\n")
        z = z+1
    elif comp == 1 and you == 'P':
        print('computer chooses Rock')
        print("you win\n")
        x = x+1
    elif comp == 1 and you == 'S':
        print('computer chooses Rock')
        print("computer win\n")
        y = y+1
    elif comp == 2 and you == 'R':
        print("computer chooses Paper")
        print("Computer win\n")
        y=y+1
    elif comp == 2 and you == 'P':
        print('computer chooses Paper')
        print("Tie\n")
        z= z+1
    elif comp == 2 and you == 'S':
        print('computer chooses Paper')
        print("You win\n")
        x =x+1
    elif comp == 3 and you == 'R':
        print("computer chooses Scissor")
        print("You win\n")
        x =x+1
    elif comp == 3 and you == 'P':
        print('computer chooses Scissor')
        print("Computer win\n")
        y = y+1
    elif comp == 3 and you == 'S':
        print('computer chooses Scissor')
        print("Tie\n")
        z = z+1

print("\n\n\n\nEnd of Chances ")
if x>y:
    print("You won", x, "games")
    print("Comp won", y, "games")
    print("Tie games", z)
    print("your ultimate winner")
elif y<x:
    print("You won", x, "games")
    print("Comp won", y, "games")
    print("Tie games", z)
    print("computer is ultimate winner")
else:
    print("You won", x, "games")
    print("Comp won", y, "games")
    print("Tie games", z)
    print("its a Tie")


