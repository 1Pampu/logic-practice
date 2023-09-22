# * Create a function that receives a decimal number and transforms it into Octal
# * and Hexadecimal.
# * - It is not allowed to use built-in functions of the programming language that
# * perform these operations directly.

hex = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
octal = [
    '0', '1', '2', '3', '4', '5', '6', '7', '10', '11',
    '12', '13', '14', '15', '16', '17', '20', '21', '22', '23',
    '24', '25', '26', '27', '30', '31', '32', '33', '34', '35',
    '36', '37', '40', '41', '42', '43', '44', '45', '46', '47',
    '50', '51', '52', '53', '54', '55', '56', '57', '60', '61',
    '62', '63', '64', '65', '66', '67', '70', '71', '72', '73',
    '74', '75', '76', '77'
]

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
    notation = ""
    while True:
        quotient = number // 8
        remainder = number % 8
        number = quotient

        notation = str(hex[remainder]) + notation

        if quotient == 0:
            break

    return notation

def convert(number):
    hexValue = toHex(number)
    octValue = toOct(number)
    print(f'The number {number} is {hexValue} in Hex and {octValue} in Octal!')


convert(255)