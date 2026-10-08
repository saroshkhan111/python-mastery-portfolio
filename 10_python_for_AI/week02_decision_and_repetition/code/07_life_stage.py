"""
Problem Statement:
Write a program to categorize a person’s life stage based on age input.

*If age < 13, print “Child”.
*If age ≥ 13 and < 18, print “Teenager”.
*If age ≥ 18 and < 60, print “Adult”.
*Otherwise, print “Senior Citizen”.

Expected Output:
Input 15 --> Teenager
Input 65 --> Senior Citizen
"""
print()
# step 1:  create a variable age and get the input from the user and convert age in integer format
while True:
    age =  int(input("Enter Your Age: "))

    # step 2:  Apply if/else condition to check stages of life
    if  age <= 0:
        print("Error: Age Canot be Negative or less than positive values!")
        continue
        print("Please Re-Enter Your Age")

    if  age <= 13:
        print("Child")
    elif age >= 13  and age < 18:
        print("Teenager")
    elif age >= 18  and age < 60:
        print("Adult")
    else:
        print("Senior Citizen")

    choice = input("Do you want to check your age again? (Y/N)").upper()
    if choice == "Y":
        continue    
    break
print()
print("Thank You for checking your age........")
print()