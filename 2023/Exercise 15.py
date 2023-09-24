# * Create a function capable of transforming Spanish into the basic language of the Star Wars universe: "Aurebesh."
# * - You can leave characters that do not exist in "Aurebesh" untranslated.
# * - It should also be capable of translating in the opposite direction.
# * Did you succeed? Mention me on twitter.com/mouredev and write something to me in Aurebesh.
# * May the Force be with you!

basic_alphabet = {
    "a": "aurek",
    "b": "besh","c": "cresh","d": "dorn","e": "esk","f": "forn","g": "grek","h": "herf","i": "isk","j": "jenth","k": "krill","l": "leth","m": "mern",
    "n": "nern","o": "osk","p": "peth","q": "qek","r": "resh","s": "senth","t": "trill","u": "usk","v": "vev","w": "wern","x": "xesh","y": "yirt",
    "z": "zerek","0": "osk","1": "krill","2": "trill","3": "mern","4": "forn","5": "vev","6": "senth","7": "cresh","8": "resh","9": "dorn"
}

def translateAurebesh(text, isAurebesh):

    tanslation = ""
    if not isAurebesh:

        for i in text:
            if i == " ":
                tanslation += " "
            else:
                tanslation += basic_alphabet[i]

    return tanslation

notAurebesh= translateAurebesh("hola como estan", False)
print(notAurebesh)