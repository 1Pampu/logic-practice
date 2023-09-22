# * Create a function that receives a decimal number and transforms it into Octal
# * and Hexadecimal.
# * - It is not allowed to use built-in functions of the programming language that
# * perform these operations directly.

hex = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]

def toHex(number):
    notation = ""
    while True:
        quotient = number // 16
        remainder = number % 16
        number = quotient

        notation = str(hex[remainder]) + notation

        if quotient == 0:
            break

    return notation

def toOct(number):
    pass

def convert(number):
    pass

n = 43
toHex(255)