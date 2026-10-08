"""
Problem Statement:
You are part of a banking system.
To approve a loan, two conditions must be met:
- The user's age must be 21 years or older.
- If the age is valid, check whether the user's monthly income is 30,000 or more.

Conditions:
- If both conditions are met, print "Loan Approved".
- If the age is valid but the income is lower, print "Income criteria not met".
- If the age is less than 21, print "Not eligible due to age". 

"""

#st 1: Print the header Loan Approval Calculator
print()
print("=" * 50)
print("           Loan Approval Calculator")
print("=" * 50)
print()

# st 1:  take user_age and convert his/her age in integer
user_age = int(input("Enter Your Age:  "))

# st 2:  take user's monthly income in the float format to cover the decimal points
monthly_income = float(input("Enter Your Monthly Income:  "))


# st 3:  Check the outer Condition first
if user_age >= 21:

    # st 4: Check the 2nd inner condition
    if user_age >= 21  and monthly_income >= 300000:
        print("Loan Approved")
    else:
        print("Income Criteria not met")
else:
    print("Not eligible due to age")
print()                