#Ask the user (via input()) for the number of tokens used and the price per 1000 tokens (in rupees).
#Convert both inputs to the correct numeric types, then compute the cost using

#and print it formatted to 2 decimal places.
#Expected Output
#Estimated cost: Rs.2.00

# step 1: Print the header Token Estimator Calculator

print("\n==== Token Estimator Calculator ====")


#step 2: Prompt the user to enter the numbers of used_tokens

tokens_used = int(input("Enter the numbers of tokens used in integer:   "))

per_price_1000 = float(input("Enter the price per 1000 token in rupees:"))

#step 3: Compute the cost
total_tk_cost = (tokens_used / 1000) * per_price_1000

#step 4: Display the Final Estimated Cost
print(f"Estimated cost: Rs. {total_tk_cost:.2f}")


