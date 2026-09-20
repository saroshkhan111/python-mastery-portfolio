print("===Token Converter Estimator===")


tokens = int(input("How many tokens did you use?  "))


perice_per_1000 = float(input("Price per token (in rupees)? "))


cost = (tokens/1000)*perice_per_1000

print(f"Estimated Price: {cost:.2f}")