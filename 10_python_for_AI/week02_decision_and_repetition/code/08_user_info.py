"""
Problem Statement
Write a program that takes a user input for a username.

*If the user presses Enter without typing anything (empty string), print “Username
 cannot be empty”.

*If the username is exactly “admin”, print “Welcome, Administrator”.

*For any other valid input, print “Welcome, [username]”

*Expected Output (Input ”):
 Username cannot be empty

*Welcome, Administrator
*Welcome, john  
"""

while True:
    print()
    user_name = input("Enter your name: ").strip()

    if user_name == "":
        print("\nUsername cannot be empty\n")

        choice = input("Do you want print your name Again? Y/N: ").upper()
        if choice == "N":
            print("Existing Program")
            break
        else:
            print("Enter Your name Again: ")
            continue
        
    elif user_name == "admin":
        print("Welcome, Administrator")
        
    else:
        print(f"Welcome, {user_name}")
    break



print()