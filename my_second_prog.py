#It is my second prog

print("Welcome to Prog Principles at Whiteclliffe")

print("This is my Second Prog")

print("######################")
print("##Part0 -- user input")
print("######################")

#str_marks = input("Please enter your marks ")
#print("marks type is: ", type(str_marks))
#n_marks = int(str_marks)

#alternate way
n_marks = int(input("Please enter your marks "))

half_marks = n_marks/2

print("half marks are ", half_marks)
#

#print("marks type after conversion is: ", type(n_marks))

print("######################")
print("##Part1 -- Boolean")
print("######################")

b_first = True
b_second = False
print ("my first var is ", b_first)
print ("my second var is ", b_second)
b_res = b_first and b_second
print ("and res is: ", b_res)

b_res = b_first or b_second
print ("or res is: ", b_res)

b_res = not b_first
print("not of first var is ", b_res)

b_res = not b_second
print("not of second var is ", b_res)

print("######################")
print("##Part2 -- while loops")
print("######################")

#while loop
j = 0

while j < 15:
    print(" while loop itr " + str(j))
    j = j  + 1

print("another while loop")

n_marks = 4
while n_marks<10:
    n_marks = int(input("Please enter your marks greater than 10 "))
    print("Your marks are ", n_marks)

    
print("another while loop")

b_continue = True
while b_continue:
    print("Please enter your name")
    str_name = input()
    #print("Please enter your marks")
    n_marks = int(input("Please enter your marks "))
    print("Your name is ", str_name, " and your marks are ", n_marks)
    print("Do you want to continue: 0/1")
    b_continue = bool(int(input()))
    
print("######################")
print("##Part4 -- for loops")
print("######################")

# for var in limit -- here range means number of times, e.g range(10) means repeat for ten times 
for i in range(10):
    print(" for loop itr " + str(i))
