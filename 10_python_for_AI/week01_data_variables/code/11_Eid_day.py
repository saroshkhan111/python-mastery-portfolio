"""
Problem Statement:
Store the number of days left until Eid as a variable equal to 12. Using the modulus operator %, print
whether this number is evenly divisible by 2 (print the boolean result, True or False).
"""



# step 2: store the number of days left untill Eid
days_left = 12

# step 3: check if the number of days left is evenly divisible by 2
is_eid_day = days_left % 2 == 0

print("\n",is_eid_day,"\n")