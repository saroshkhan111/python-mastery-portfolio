import random

print("=========== Welcome to the Guess the Number Game ===========")

while True:                                  
    secret_number = random.randint(0, 100)
    max_attempts = 4
    won = False

    for attempt in range(max_attempts):   # <-- INNER loop (attempts)
        print(f"Attempt {attempt + 1} of {max_attempts}")
        user_guess = int(input("Enter your guess [0 to 100]: "))

        if user_guess == secret_number:
            print(f"Congratulations! You guessed it in {attempt + 1} attempts.")
            won = True
            break
        elif user_guess < secret_number:
            print("Your guess is too low, try again.")
        else:
            print("Your guess is too high, try again.")

    if not won:
        print(f"Game Over! The correct number was {secret_number}.")

    
    play_again = input("Do you want to play again? (yes/no): ").lower().strip()

    if play_again != "yes" and play_again != "y":
        print("Thanks for playing! Goodbye ")
        break       