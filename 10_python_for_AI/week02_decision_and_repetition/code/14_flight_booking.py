"""
Problem Statement:
Flight Boarding Pass: Check if the passenger has a valid "Ticket" (True/False).
If yes, check "Seat Class" ("Business" or "Economy"). If Business, print "Priority
Boarding". If Economy, check if they have "Priority Status" (True/False). If
yes, print "Priority Boarding", else print "Regular Boarding". If no ticket,
print "Denied Boarding".
"""

print()
print("=" * 50)
print("    Flight Booking Priority System Program")
print("=" * 50)
print()

# Step 1: Check Ticket
ticket = input("Do you have a ticket (Yes/No)? ").strip().lower()

if ticket == "yes":
    # Step 2: Check Seat Class (only if ticket is valid)
    seat_class = input("\nWhat is Your Seat Class (Business/Economy)? ").strip().lower()
    
    if seat_class == "business":
        print("\nPriority Boarding")
        
    elif seat_class == "economy":
        # Step 3: Check Priority Status (only if economy)
        user_per = input("\nDo you have a priority Status (Yes/No)? ").strip().lower()
        
        if user_per == "yes":
            print("\nPriority Boarding")
        else:
            print("\nRegular Boarding")
            
    else:
        print("\nInvalid Seat Class entered.")
else:
    print("\nDenied Boarding")

print()