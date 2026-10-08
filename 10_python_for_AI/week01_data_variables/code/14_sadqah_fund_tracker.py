"""
A charity fund started with Rs. 15000 and received 3 donations of Rs. 500, Rs. 1200, and Rs. 750.
Using variables and arithmetic, compute the new total and print it as currency formatted to 2 decimal
places using an f-string.
"""


# step 1: create a variable and store the initial fund_amount

initial_fund_amount = 15000
donation_1 = 500
donation_2 = 1200
donation_3 = 750

# step 2: compute the new total
new_total = initial_fund_amount + donation_1 + donation_2 + donation_3

# step 3: print the new total as currency formatted to 2 decimal places using an f-string
print(f"\nNew total fund amount: Rs. {new_total:.2f}\n")