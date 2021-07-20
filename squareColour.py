"""
iQualify Challenge 1: What colour is that square?

Given a standard chessboard where each row is a number 1 - 8
and each column is a letter from a - h like below:

 8 |_|*|_|*|_|*|_|*|
 7 |*|_|*|_|*|_|*|_|
 6 |_|*|_|*|_|*|_|*|
 5 |*|_|*|_|*|_|*|_|
 4 |_|*|_|*|_|*|_|*|
 3 |*|_|*|_|*|_|*|_|
 2 |_|*|_|*|_|*|_|*|
 1 |*|_|*|_|*|_|*|_|
    a b c d e f g h

get a row and a column and return if its black or white
@author John Wright, 20210556
18 May 2021.

"""


# function to return the colour of space selected on a chess board.
def get_space(col, row):
    if (col == 'a') or (col == 'c') or (col == 'e') or (col == 'g'):  # check which column the value is in
        if row % 2 == 1:  # odd rows
            return "Black"  # i.e 'a' is only black on odd rows.
        else:
            return "White"
    else:  # must be 'b' or 'd' or 'f' or 'h'
        if row % 2 == 0:  # even rows
            return "Black"
        else:  # odd rows
            return "White"


c = input("What column is the space on? (a-h) ")  # get column
r = int(input("What row is the space on? (1-8) "))  # get row

print(f"Selected space is {c.upper()}{r}")  # state the selected space
v = get_space(c, r)  # preform the function
print(f"Your space is {v}")  # print the result

# Test case assertion One:
# Input of column a and row 1 should return "Black"
print("Test case 1: A1. Returns " + get_space("a", 1) + " (expected 'black')")

# Test case assertion two:
# Input column b and row 1 should return "White"
print("Test case 2: B1. Returns " + get_space("b", 1) + " (expect 'white')")

# Test case assertion three:
# Input column b and row 1 should return "White"
print("Test case 3: E2. Returns " + get_space("e", 2) + " (expect 'white')")

# Test case assertion four:
# Input column b and row 1 should return "Black"
print("Test case 4: F8. Returns " + get_space("f", 8) + "(expect 'black')")

