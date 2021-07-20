print("Welcome to the Bingo Game...\n")
print("In the game of Bingo, when a player enters a number")
print("it is checked against the following list:")
n_bingolist = [7,26,40,58,73,14,22,34,55,68]
print(n_bingolist)
print("if the number exists in the above list it is crossed out")
print("When all the numbers have been crossed out, the player receives a BINGO from the system")
n_listcount=(len(n_bingolist))
i = 0
while i < (n_listcount):    # loop counter less than the listcount
  n_input=int(input("Please enter a random number between 1 and 80 inclusive:...\n")) #input a no.
  print("Thank you for your input\n")
  if n_input in n_bingolist:
    n_bingolist.remove(n_input) # strike off numbers off the list if there is a match
    if (len(n_bingolist)) != 0: # if the list is not empty then increment by 1
      i += 1
    else:                      # else Bingo
      print("Bingo!!!")
      break


