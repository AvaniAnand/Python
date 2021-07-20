#My second prog
#while loop
print("######################")
print("##Part0 -- loops")
print("######################")

# loop condition
loop_continue = True
while loop_continue:
    n_user_no = int(input("Please enter a no between 100 and 1000 "))
    if n_user_no >=100 and n_user_no < 1000:
        loop_continue = False