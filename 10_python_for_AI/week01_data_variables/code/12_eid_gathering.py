"""
Problem Statement:
Ask the user, using input(), how many family members will attend an Eid gathering. Convert the
input to an integer, add 2 (for guests), and print the final total using an f-string.
"""

# step 1: Prompt the user to enter the guest values

total_guest = int(input("Enter the total familiy members who will attend the Eid gathering: "))

# step 2: Add 2 for guests and print the final total using an f-string

print(f"\nTotal attendees: {total_guest + 2}\n")