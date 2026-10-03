"""
Write a program that checks if a student passes. A student passes if marks >= 40 AND
attendance >= 75. Take both inputs from the user.
1 Enter marks : 50
2 Enter attendance %: 80
3 Student passed : True
"""

# st 1: prompt the user to enter their marks and attendence

user_marks = float(input("Enter your marks: "))

user_att = float(input("Enter attendence %: "))


# st 2: calculate the users and percentage

passed = user_marks >= 40 and user_att >= 75

print(f"\nStudent Passed : {passed}\n")

