"""
Movie Ticket and Genre Ticket
"""

print("=" * 45)
print("       CINEMA TICKET VERIFICATION")
print("=" * 45)

# st 1: Ticket check
has_ticket = input("\nDo you have a ticket [Yes|No]? ").strip().lower()

# st 2: check first outer condition
if has_ticket == "yes":

    # st 3: check the user_age
    age = int(input("\nEnter Your age: "))
    if age < 18:
        print("\nSorry, you must be at least 18 to watch these movies.")

    else:
        # st 4: check the movie genre
        movie_genre = input("\nEnter Your genre [Horror|Action]? ").strip().lower()
        if movie_genre == "action":
            print("\nEnjoy the action movie")

        elif movie_genre == "horror":
            if age < 25:
                print("\nToo scary! Watch with parents.")
            else:
                print("\nEnjoy the horror movie")
        else:
            print("\nPlease Select the Correct genre")                
            
else:
    print("\nPlease buy a ticket first.")                

print()