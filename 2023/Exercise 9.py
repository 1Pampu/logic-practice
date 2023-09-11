# * Create 3 functions, each responsible for detecting whether a string of
# * text is a heterogram, an isogram, or a pangram.
# * - You must look up the definition of each of these terms.

import string

def isHeterogram(text):
    letters = []
    for letter in text:
        if letter != " ":
            if letter.upper() in letters:
                return False
            else:
                letters.append(letter.upper())
    return True

def isIsogram(text):
    count = {}
    for letter in text:
        if letter != " ":
            if letter.upper() in count:
                count[letter.upper()] += 1
            else:
                count[letter.upper()] = 1

    highier = max(count.values())
    if highier == 1:
        return False

    for value in count.values():
        if value != highier:
            return False

    return True

def isPangram(text):
    letters = string.ascii_uppercase
    letters = [ letter for letter in letters]
    for letter in text:
        if letter.upper() in letters:
            letters.remove(letter.upper())
    if len(letters) > 0:
        return False
    return True

Heterogram = "Hi You"
Isogram = "Anna"
Pangram = "The quick brown fox jumps over the lazy dog "

print(isHeterogram(Heterogram))
print(isIsogram(Isogram))
print(isPangram(Pangram))