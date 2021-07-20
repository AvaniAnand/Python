#My second prog
#while loop
print("######################")
print("##Part0 -- if-else-if")
print("######################")

# if - else - if
n_user_no = int(input("Please enter a no ")) 

#if condition :
if n_user_no >=800:
    print("Balance is greater than 800")
    new_no = n_user_no + 1234
    print("New no is ", new_no)
elif n_user_no >=700:
    print("Balance is greater than 700 and less tha 800")
else:
    print("Balance is less tha 700")