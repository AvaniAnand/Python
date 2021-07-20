print("Welcome to the Grade calculator program...\n")
n_projectscore=int(input("Please enter the project score:"))
n_examscore=int(input("Please enter the exam score:"))
print("Thank you for your input\n")  # input the score
n_finalscore: float=(n_projectscore*0.50)+(n_examscore*0.50) #calculate the final score
print("The final score is:")
print(float(n_finalscore))
if n_finalscore>=80:        #assign the grade
    print("The final grade is: A")
elif n_finalscore >=70 and n_finalscore<79:
    print("The final grade is: B")
elif n_finalscore >= 60 and n_finalscore < 69:
    print("The final grade is: C")
elif n_finalscore >= 50 and n_finalscore < 59:
    print("The final grade is: D")
else:
    print("Sorry you have failed!")
