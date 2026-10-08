"""
Problem Statement:
Theme Park Ride: Height must be ≥48 inches. If height is valid, check if age
is ≥ 12. If both true, print "Can ride alone". If height valid but age <12, print
"Must ride with an adult". If height <48, print "Cannot ride".
"""

# st print the header Ride Theme Program

print("=" * 50)
print("       Ride Theme Software Checker")
print("=" * 50)
print()


# st 1: Get the Height from the user

height = float(input("Enter Your Height: "))

# st 2: Get the age from the user
age = int(input("\nEnter Your age: "))


# st 3: Apply first condition to check 
if height >= 48:

    # st 4: check the age of user
    if age >= 12:
        print("Can ride alone")
    else:
        print("Must ride with an adult")    
else:
    print("Cannot ride")
    
print()    