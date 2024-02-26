# * Create a function capable of transforming Spanish into the basic language of the Star Wars universe: "Aurebesh."
# * - You can leave characters that do not exist in "Aurebesh" untranslated.
# * - It should also be capable of translating in the opposite direction.
# * Did you succeed? Mention me on twitter.com/mouredev and write something to me in Aurebesh.
# * May the Force be with you!

basic_alphabet = {
    "a": "aurek","b": "besh","c": "cresh","d": "dorn","e": "esk","f": "forn","g": "grek","h": "herf","i": "isk","j": "jenth",
    "k": "krill","l": "leth","m": "mern","n": "nern","o": "osk","p": "peth","q": "qek","r": "resh","s": "senth","t": "trill",
    "u": "usk","v": "vev","w": "wern","x": "xesh","y": "yirt","z": "zerek"
}

def translateAurebesh(text, isAurebesh):

    tanslation = ""
    if not isAurebesh:
        # Translate to Aurebesh
        for letter in text:
            for key, value in basic_alphabet.items():
                if letter == key:
                    tanslation += value
                    break
            else:
                tanslation += letter

    else:
        # Translate to spanish
        text_list = text.split(" ")
        for word in text_list:
            letter_list = []
            letters = 0

            for key, value in basic_alphabet.items():
                if value in word:
                    letter_list.append(key)
                    letters += 1

            while letters > 0:
                for letter in letter_list:
                    if word.startswith(basic_alphabet[letter]):
                        tanslation += letter
                        word = word.replace(basic_alphabet[letter], "")
                        letters -= 1

            tanslation += " "

    return tanslation


notAurebesh = translateAurebesh("hi how are you?", False)
print(notAurebesh)

Aurebesh = translateAurebesh("herfisk herfoskwern aurekreshesk yirtoskusk?", True)
print(Aurebesh)