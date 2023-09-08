# * Write a program that, given a number, checks and displays if it is prime, Fibonacci, and even.
# * Examples:
# * - With the number 2, it will say: "2 is prime, Fibonacci, and even"
# * - With the number 7, it will say: "7 is prime, not Fibonacci, and odd"

def prime(x):
    if x <= 1:
        return "Not Prime"

    n = 2
    while True:
        if n == x:
            return "Prime"
        elif not x % n:
            return "Not Prime"

        n += 1

def fibonacci(x):
    secuence = [0,1]
    while True:
        if x in secuence:
            return "Fibonacci"
        elif x < secuence[-1]:
            return "Not Fibonacci"

        n = secuence[-1] + secuence[-2]
        secuence.append(n)

def even(x):
    if not x % 2:
        return "Even"
    else:
        return "Odd"

myNumber = int(input("Your number: "))
print(f"{myNumber} is {prime(myNumber)}, {fibonacci(myNumber)} and {even(myNumber)}")