"""
Write a program that asks the user to enter their age. Convert the input
to an integer. If the age is 18 or older, print “Eligible to vote”. Otherwise, print “Not
eligible”.
"""

print()
while True:
    # step 1: get the input from the user
    age = int(input("Enter Your age: "))

    # step 2: check age cannot be negative
    if age <= 0:
        print("Error Age Cannot be negative or Zero")

    #step 3: Ask the user to re-enter age again
        choice = input("Do you want to check your age again (Y/N)?: ").upper()
        if choice != "Y":
            break
        continue    

        
    else:
        #step 4: check the eligibility for vote
        if age >= 18:
            print("You are Eligible for Vote")

        else:
            print("You are not Eligible for Vote")

        choice = input("Do you want to check your age again (Y/N)?: ").upper()
        if choice != "Y":
            break
        continue       


    
print("\nThank You for using Age Verification System......")
print()            