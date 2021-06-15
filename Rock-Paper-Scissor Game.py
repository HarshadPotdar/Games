#Rock, Paper, and scissor game

import random

def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == 'R':
        if you == 'P':
            return True
        elif you == 'S':
            return False
    elif comp == 'P':
        if you == 'R':
            return True
        elif you == 'S':
            return False
    elif comp == 'S':
        if you == 'R':
            return True
        elif you == 'P':
            return False

print("computer turn Rock(R) , Paper(P), Scissor(S)")
randomnumber = random.randint(1,3)
if randomnumber == 1:
    comp = 'R'
elif randomnumber == 2:
    comp = 'P'
elif randomnumber == 3 :
    comp = 'S'

you = input("roll the dice: \n")
a = gamewin(comp, you)

print(f"computer choose: \n{comp}")
print(f"you choose: \n{you}")

if a == None :
    print("the game is a tie")
elif a == True:
    print("You win")
elif a == False:
    print("computer won")
