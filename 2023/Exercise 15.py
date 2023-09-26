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

        for i in text:
            if not i in basic_alphabet.keys():
                tanslation += i
            else:
                tanslation += basic_alphabet[i]

    if isAurebesh:

        lista = []
        for letter, seccuence in basic_alphabet.items():
            if seccuence in text:
                lista.append(letter)

    return tanslation


notAurebesh = translateAurebesh("hi how are you?", False)
print(notAurebesh)

Aurebesh = translateAurebesh("herfisk herfoskwern aurekreshesk yirtoskusk?", True)
print(Aurebesh)