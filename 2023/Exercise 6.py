# * Create a program that calculates who wins more rounds of Rock, Paper, Scissors, Lizard, Spock.
# * The result can be: "Player 1", "Player 2", or "Tie" (a draw).
# * The function receives a list containing pairs, representing each play.
# * The pair can contain combinations of "🗿" (rock), "📄" (paper),
# * "✂️" (scissors), "🦎" (lizard), or "🖖" (Spock).
# * Example: Input: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Result: "Player 2".
# * You should look up information on how to play with these 5 possibilities.

table = {
    "🗿":["🦎","✂️"],
    "📄":["🗿","🖖"],
    "✂️":["📄","🦎"],
    "🦎":["🖖","📄"],
    "🖖":["✂️","🗿"]
}

def calculate(list):
    player1 = 0
    player2 = 0
    for tuple in list:
        print(tuple)
        if tuple[0] == tuple[1]:
            pass
        elif tuple[1] in table[tuple[0]]:
            player1 += 1
        elif tuple[0] in table[tuple[1]]:
            player2 += 1

    if player1 == player2:
        print("Tie")
    elif player1 > player2:
        print("Player 1")
    elif player1 < player2:
        print("Player 2")

game = [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]
calculate(game)