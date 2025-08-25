def setOrNot(number, n):

    if number & (1 << (n - 1)):
        print("\nSet")
    else:
        print("\nNot Set")

number = int(input("Enter your number : "))
n = int(input("Enter bit number : "))
setOrNot(number, n)