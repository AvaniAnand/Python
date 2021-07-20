"""
iQualify Challenge 2: Name that triangle!

A triangle is classified on the length of its sides:
If 3/3 sides are the same its an equilateral triangle.
If 2/3 sides are the same its an isosceles triangle.
If no sides are the same its a scalene triangle.

Get three lengths from the user, and return what type of triangle they have
i.e (10,10,20) = isosceles.

@author John Wright <20210556>
18 May 2021.
"""


# Function to show what sort of triangle you have
def get_triangle(s1, s2, s3):
    if (s1 == s2) and (s2 == s3):  # if all three sides are the same
        return "An equilateral triangle"
    elif (s1 != s2) and (s1 != s3) and (s2 != s3):  # if all three sides are different
        return "A scalene triangle"
    else:  # all other cases must have two the same
        return "An isosceles triangle"


# Run the program to get user input and check for the triangle type.
print("Put in three numbers to calculate the type of triangle you have:")
side1 = int(input("Enter the length of the first side: "))
side2 = int(input("Enter the length of the second side: "))
side3 = int(input("Enter the length of the third side: "))
print(f"You're triangle is {get_triangle(side1, side2, side3)}")


# Test case assertions:
print("Test case assertions:")
print(f"Test case 1: 10,10,10. Returns [{get_triangle(10, 10, 10)}]. Expected 'Equilateral'")
print(f"Test case 1: 10,10,11. Returns [{get_triangle(10, 10, 11)}]. Expected 'Isosceles'")
print(f"Test case 1: 10,11,12. Returns [{get_triangle(10, 11, 12)}]. Expected 'Scalene'")


