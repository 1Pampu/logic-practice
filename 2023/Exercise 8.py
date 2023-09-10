# * Create a pseudo-random number generator between 0 and 100.
# * - You cannot use any "random" (or similar) function of the selected programming language.
# * It's more complicated than it seems...

import time

def random():
    number = time.time_ns() % 101
    return number

print(random())