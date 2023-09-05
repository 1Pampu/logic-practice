# * Write a program that takes input text and transforms natural language into
# * "hacker language" (actually known as "leet" or "1337" speak). This language
# * is characterized by substituting alphanumeric characters.
# * - Use this table (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
# *   with the alphabet and numbers in "leet" speak.
# *   (Use the first option for each transformation. For example, "4" for "a".)

leet = {"A": "4", "B": "I3", "C": "[", "D": ")", "E": "3", "F": "|=", "G": "&", "H": "#", "I": "1",
        "J": ",_|", "K": ">|", "L": "1", "M": "/\/\\", "N": " ^/", "O": "0", "P": " |*", "Q": "(_,)",
        "R": "I2", "S": "5", "T": "7", "U": "(_)", "V": "\/", "W": "\/\/", "X": "><", "Y": "j", "Z": "2",
        "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b", "7": "T", "8": "B", "9": "g", "0": "o"}

text = input("Write the text to translate: ")
translated = ""

for letter in text:
    if letter == " ":
        translated += " "
    elif letter.isnumeric():
        translated += leet[letter]
    else:
        translated += leet[letter.upper()]

print(translated)