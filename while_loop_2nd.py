#My second prog
#while loop
print("######################")
print("##Part0 -- loops")
print("######################")

# loop condition
n_user_loop_cond = int(input("Please enter a no for loop condition ")) 
n_user_loop_cond_2nd = n_user_loop_cond
#loop condition :
#while condition: #untill the condition is true it will continue

while n_user_loop_cond >0:
    print("Loop condition value is", n_user_loop_cond)
    n_user_loop_cond = n_user_loop_cond - 1

print("An other way to do while loop")
n_itr = 0    
while n_itr < n_user_loop_cond_2nd:
    n_itr = n_itr + 1
    print("I am on iteration no ", n_itr)