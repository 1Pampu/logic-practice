# * Write a program that displays in the console (with a print) the
# * numbers from 1 to 100 (both inclusive, with a line break between
# * each print), replacing the following:
# * - Multiples of 3 with the word "fizz."
# * - Multiples of 5 with the word "buzz."
# * - Multiples of 3 and 5 at the same time with the word "fizzbuzz."

for x in range(1,101):

    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    elif x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)