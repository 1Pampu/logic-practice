# * Write a program that shows how a tennis game unfolds and who has won it.
# * The program will receive a sequence consisting of "P1" (Player 1) or "P2" (Player 2), indicating who wins each point of the game.

# * - The scores in a game are "Love" (zero), 15, 30, 40, "Deuce" (tie), advantage.
# * - Given the sequence [P1, P1, P2, P2, P1, P2, P1, P1], the program would display the following:
# *   15 - Love
# *   30 - Love
# *   30 - 15
# *   30 - 30
# *   40 - 30
# *   Deuce
# *   Advantage P1
# *   Player 1 has won

# * - If you wish, you can handle errors in the input data.
# * - Consult the rules of the game if you have doubts about the scoring system.

score = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]    # Advantage P1
#score = ["P1", "P1", "P1", "P1"]    # 40 - 0
#score = ["P1", "P1", "P1","P2","P2","P2","P1","P2","P2","P2",]   # Advantage P1 , Advantage P2, Win p2

pointsTranslates = {0:"Love",1:"15",2:"30",3:"40"}
P1points = 0
P2points = 0
Deuce = False

def winner(P1,P2):
    if P1 == 5:
        winner= 1
    if P2 == 5:
        winner= 2
    print(f"Player {winner} has won")

for x in score:

    if x == "P1":
        P1points += 1
        if P1points == 4 and Deuce == False:
            P1points += 1
        elif P1points == 4 and P2points == 4:
            P2points -= 1
    if x == "P2":
        P2points += 1
        if P2points == 4 and Deuce == False:
            P2points += 1
        elif P2points == 4 and P1points == 4:
            P1points -= 1

    if P1points == 3 and P2points == 3:
        print("Deuce")
        Deuce = True
    elif Deuce == True:
        if P1points == 4:
            print("Advantage P1")
        elif P2points == 4:
            print("Advantage P2")

    if P1points == 5 or P2points == 5:
        winner(P1points,P2points)
    elif Deuce == False:
        print(f"{pointsTranslates[P1points]} - {pointsTranslates[P2points]}")