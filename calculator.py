"""
Programming Principles python practice:

Calculator:
Please write a calculator program that can do the following:
1.Get a number, less than 100, from the user.
2.Get another number, between 100 and 1000, from the user.
3.Get a mathematical operation from the user, e.g. +, -, *, /, %.
4.Perform the mathematical operation and display the result.
5.Repeat step 1 to 4 until user wants to quit.

@author John Wright <20210556?
19 May 2021.

"""
running = True

# run calculator until user quits
while running:

    # Alternately:
    # Get first number
    # num1 = int(input("Please enter a number between 1 and 100: "))
    # checks the number is valid
    # if num1 > 100 or num1 < 1:
    # print(f"{num1} outside requested bounds. Starting again")
    # continue  # restart loop

    num1 = 0
    while num1 > 100 or num1 < 1:
        num1 = int(input("Enter a number between 1 and 100: "))
        if num1 > 100 or num1 < 1:
            print("Invalid input.")

    # Alternatively:
    # Get second number
    # num2 = int(input("Please enter a number between 100 and 1000: "))
    # checks the number is valid
    # if num2 < 100 or num2 > 1000:
        # print(f"{num2} outside requested bounds Starting again")
        # continue  # restart loop

    num2 = 0
    while num2 > 1000 or num2 < 100:
        num2 = int(input("Enter a number between 100 and 1000: "))
        if num2 > 1000 or num2 < 100:
            print("Invalid input.")

    # Get operator
    op = input("Please enter an operator(+, -, /, *, %): ")

    # Check operator
    if op == '+':
        total = num1 + num2
        print(f"{num1} + {num2} = {total}")
    elif op == '-':
        total = num1 - num2
        print(f"{num1} - {num2} = {total}")
    elif op == '/':
        total = num1 / num2
        print(f"{num1} / {num2} = {round(total,2)} (2dp)")
    elif op == '*':
        total = num1 * num2
        print(f"{num1} * {num2} = {total}")
    elif op == '%':
        total = num1 % num2
        print(f"{num1} % {num2} = {total}")
    else:
        print("invalid operator Try equation again")

    # User can try again or exit the program
    replay = input("press x to quit or any other key to continue:")
    if replay.capitalize() == "X":
        running = False
