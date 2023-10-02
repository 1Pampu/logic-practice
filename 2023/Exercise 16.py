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

def stairs(number):

    if number == 0:
        print("__")

    elif number > 0:

        stair = []
        floor = []
        for i in range(0,number):
            stair.append("  ")
            floor.append("  ")
        stair.append("_|")
        floor.append("  _")

        for i in floor:
            print(i,end="")
        print()

        for i in range(0,number):
            for x in stair:
                print(x,end="")
            print()
            stair.pop(0)

    elif number < 0:
        pass

stairs(4)