#  * Write a program capable of generating passwords randomly.
#  * You will be able to configure password generation with the following parameters:
#  * - Length: Between 8 and 16.
#  * - With or without uppercase letters.
#  * - With or without numbers.
#  * - With or without symbols.
#  * (You can combine all these parameters together)

import random
import string
bools = [True,False]

# Length = int, upperCase = bool, numbers = bool, symbols = bool
def generatePassword(length, upperCase, numbers, symbols):

    if length >= 8 and length <= 16:

        passwordList = []
        for x in range(0,length):
            passwordList.append(random.choice(string.ascii_lowercase))

        if upperCase:
            for x in range(0,length):
                if random.choice(bools):
                    passwordList[x] = passwordList[x].upper()

        if numbers:
            for x in range(0,length):
                if random.choice(bools):
                    passwordList[x] = random.randint(0,9)

        if symbols:
            for x in range(0,length):
                if random.choice(bools):
                    passwordList[x] = random.choice(string.punctuation)

        password = ""
        for letter in passwordList:
            password += str(letter)
            pass

        return password

    else:
        print("Introduce a valid lenght!")

rLenght = random.randint(8,16)
rUpperCase = random.choice(bools)
rNumbers = random.choice(bools)
rSymbols = random.choice(bools)
print(f"Lenght: {rLenght} \nUpperCase: {rUpperCase}\nNumbers: {rNumbers}\nSymbols: {rSymbols}")

newPassword = generatePassword(rLenght,rUpperCase,rNumbers,rSymbols)
print(newPassword)