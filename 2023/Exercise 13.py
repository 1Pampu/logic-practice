# * Create a small game that involves guessing words within a maximum number of attempts:
# *   - The game starts by presenting a randomly incomplete word
# *     - For instance, "m_ur_d_v," along with the remaining number of attempts
# *   - The user can input only a single letter or a word (of the same length as the word to be guessed)
# *     - If they type a letter and guess correctly, that letter is revealed in the word. If they make an incorrect guess, one attempt is deducted.
# *     - If they enter a complete word and guess correctly, the game ends. If not, one attempt is deducted.
# *     - If the attempt counter reaches 0, the player loses.
# *   - The word must randomly conceal letters, and it should never initially hide more than 60%.
# *   - You are free to use any words you prefer and choose the number of attempts you find suitable.

import random

class GuessGame():
    def __init__(self):
        words = ["Elephant","Guitar","Sunshine","Keyboard"]
        self.misteryWord = random.choice(words)
        self.attempts = 3
        self.win = False
        self.mistery = ""
        self.hidesIndex = []
        self.hidesLetters = []

        hide = len(self.misteryWord) // 2
        for i in range(0,hide):
            toHide = random.randint(0,(len(self.misteryWord) -1))
            if not toHide in self.hidesIndex:
                self.hidesIndex.append(toHide)
                self.hidesLetters.append(self.misteryWord[toHide].upper())

        for i in range(0,len(self.misteryWord)):
            if i in self.hidesIndex:
                self.mistery += "_"
            else:
                self.mistery += self.misteryWord[i]


    def guess(self,text):
        if self.attempts > 0 and self.win == False:

            if text.capitalize() == self.misteryWord:
                self.win = True
                self.mistery = self.misteryWord
                return "Winner!"

            elif len(text) == len(self.misteryWord):
                self.attempts -= 1
                if self.attempts == 0:
                    return "You have 0 attempts left. You lost!"
                else:
                    return f"Nice try, you have {self.attempts} left"
            elif len(text) != 1:
                return "Type a valid guess!"

            else:
                if text.upper() in self.hidesLetters:
                    indexT = self.hidesLetters.index(text.upper())
                    index = self.hidesIndex[indexT]
                    newMistery = ""
                    for i in range(0,len(self.mistery)):
                        if i == index:
                            newMistery += text.lower()
                        else:
                            newMistery += self.mistery[i]

                    self.mistery = newMistery
                    self.hidesLetters.pop(indexT)
                    self.hidesIndex.pop(indexT)

                    if self.mistery.lower() == self.misteryWord.lower():
                        self.win = True
                        return "Winner!"

                    return f"That's correct, keep it going"


                else:
                    self.attempts -= 1
                    if self.attempts == 0:
                        return "You have 0 attempts left. You lost!"
                    else:
                        return f"Nice try, you have {self.attempts} left"

        elif self.attempts == 0 and self.win == False:
            return "You already lost!"
        else:
            return "You already won!"

    def misteryPreview(self):
        return self.mistery

newGame = GuessGame()

print("The game started!")
print(newGame.misteryPreview())

while True:
    myGuess = input("Guess: ")
    print(newGame.guess(myGuess))

    if newGame.attempts == 0 or newGame.win == True:
        break

    print(newGame.misteryPreview())


