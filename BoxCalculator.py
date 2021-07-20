print("Welcome to the Box calculator program...\n")
n_items=int(input("Please enter total items, greater than or equal to 5:"))
print("Thank you for your input\n")
n_largeboxesused: int=n_items/5 #calculate the number of large boxes
n_remainingboxes: int = n_items % 5  #calculate the remaining number of boxes
n_mediumboxesused:int=(n_remainingboxes / 3) #calculate the no. of medium boxes
n_remainingboxes:int=(n_remainingboxes % 3)
n_smallboxesused:int=(n_remainingboxes / 1)  #calculate the no. of small boxes
print("The number of large boxes used are:")
print(int(n_largeboxesused))
print("The number of medium boxes used are:")
print(int(n_mediumboxesused))
print("The number of small boxes used are:")
print(int(n_smallboxesused))



