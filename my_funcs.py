print("######################")
print("##Part1: Functions")
print("######################")

# def function_name():

def my_func():
    print("My first function in Python")
    print("I'm writing another line inside my_func")
    
#call your function
my_func()

#use multiple times
for i in range(10):
    my_func()



def sum_num_only(n_num1, n_num2):
    n_sum = n_num1 + n_num2
    print("inside function sum_num: sum of numbers is " + str(n_sum))
    

sum_num_only(8, 9)

num_first = int(input("Please enter your first no "))
num_second = int(input("Please enter your second no "))

#call function
sum_num_only(num_first, num_second)

def sum_num_return(n_num1, n_num2):
    n_sum = n_num1 + n_num2
    return n_sum

num_first = int(input("Please enter your first no "))
num_second = int(input("Please enter your second no "))

n_res = sum_num_return(num_first, num_second)
print("The returned sum is " + str(n_res))
