# Write a Python Program to Input a Number, if it is not a Number Generate an Error Message.
while True:
    try:
        a = int(input("Input a Number: "))
        break

    except ValueError:
        print('\nThis is not a Number. Try Again...')
        print()
