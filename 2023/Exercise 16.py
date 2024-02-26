#  * Create a function that draws a staircase based on its number of steps.
#  * - If the number is positive, it will be ascending from left to right.
#  * - If the number is negative, it will be descending from left to right.
#  * - If the number is zero, it will draw two underscores (__).

#  * Example: 4
#  *         _
#  *       _|
#  *     _|
#  *   _|
#  * _|

#  * Example: -4
#  * _
#  *  |_
#  *    |_
#  *      |_
#  *        |_


def stairs(number):

    if number == 0:
        print("__")

    elif number > 0:
        length = number * 2
        print(" " * length + "_")
        for i in range(number):
            length -= 2
            print(" " * length + "_|")

    elif number < 0:
        print("_")
        length = 1
        number = abs(number)
        for i in range(number):
            print(" " * length + "|_")
            length += 2

stairs(4)
stairs(-4)