"""
Write a program that asks the user for their birth year, calculates their age, and prints it using
an f-string with proper formatting

Expected Output (if user enters 2000):

Enter your birth year : 2000
2 You are approximately 25 years old in 2025.
"""



# prompt the user to enter their age
birth_year = int(input("Enter your birth in the integer format:  "))

# Calculate the user's age

current_year = 2025

age = (current_year - birth_year)

print(f"\nYou are approximately {age} years old in {current_year}.\n")
