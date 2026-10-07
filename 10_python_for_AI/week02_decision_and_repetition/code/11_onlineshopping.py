"""
Problem Statement:
Check if the user is a "Premium Member". If yes,
check if the cart value is >5000. If both are true, print "20% Discount Applied".
If member but cart ≤5000, print "10% Discount Applied". If not a member,
print "No Discount".
"""

# st 1: print the header Shopping Cart Member Ship Status
print()
print("=" * 50)
print("      Shopping Cart Membership Status Checker")
print("=" * 50)

# st 2: Check the User is a permium or Not

# st 3: get the Input from the User
user_input = input("Enter Your Cart Status (True/False)? ").strip().lower()

# st 4: check the card card status
is_permium = (user_input == "true")

# st 5:  get the card amount from the user
cart_amount = int(input("\nEnter Your Cart_amount: "))
print()

# st 6: Check the 1st condition user is permium or not
if is_permium:

    # st 7: Apply the discount based on the condition
    if cart_amount > 5000:
        print("20% Discount Applied")
    else:
        print("10% Discount Applied")

else:
    print("No Discount")
print()                 