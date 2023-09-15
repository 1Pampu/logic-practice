# * Create a function that is capable of detecting if a Friday the 13th exists in the specified month and year.
# * - The function will receive the month and year and return true or false.

import calendar

def isFriday13(year,month):
    if calendar.weekday(year,month,13) == 4:
        return True
    return False

myYear = 2020
myMonth = 3
print(isFriday13(myYear,myMonth))