# * Create a program that simulates the behavior of the sorting hat from the
# * magical universe of Harry Potter.
# * - If possible, it will ask 5 questions (at a minimum) through the terminal.
# * - Each question will have 4 possible answers (also to be selected through the terminal).
# * - Based on the answers to the 5 questions, you should design an algorithm that
# *   places the student into one of the 4 Hogwarts houses (Gryffindor, Slytherin, Hufflepuff, and Ravenclaw).
# * - Take into account the traits of each house when asking questions and creating the sorting algorithm.
# * For example, in Slytherin, ambition and cunning are rewarded.

questions = { 1:[
    "How would you define yourself?",
    "1- Ambitious",
    "2- Brave",
    "3- Loyal",
    "4- Wise"
], 2:[
    "What is your favorite class?",
    "1- Defense Against the Dark Arts",
    "2- Flying",
    "3- Fantastic Beasts",
    "4- Potions"
], 3:[
    "Where would you spend the most time?",
    "1- In the common room",
    "2- Exploring",
    "3- Greenhouse",
    "4- Library"
], 4:[
    "What is your favorite color?",
    "1- Green",
    "2- Red",
    "3- Yellow",
    "4- Blue"
], 5:[
    "What is your pet?",
    "1- Snake",
    "2- Owl",
    "3- Cat",
    "4- Toad"
]}

import random

class SortingHat():
    def __init__(self):
        self.housePoints = {1:0, 2:0, 3:0, 4:0}
        self.houseNames = {1:"Slytherin", 2:"Gryffindor", 3:"Hufflepuff", 4:"Ravenclaw"}

    def answer(self,option):
        try:
            option = int(option)
        except:
            return "Not a valid answer"
        if option > 4: return "Not a valid answer"

        self.housePoints[option] += 1
        return "Answer recieved"

    def chosenHouse(self):
        maxPoints = max(self.housePoints.values())
        mostRated = []
        for key,value in self.housePoints.items():
            if value == maxPoints:
                mostRated.append(key)

        mostRated = random.choice(mostRated)
        return f"You belong to: {self.houseNames[mostRated]}!"

MagicHat = SortingHat()

for lists in questions.values():
    for text in lists:
        print(text)
    MagicHat.answer(input("Type your answer here: "))

house = MagicHat.chosenHouse()
print(house)

