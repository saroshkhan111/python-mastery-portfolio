"""
Write a complete program that:

1. Asks user for weight in kg and height in meters
2. Calculates BMI using formula: BMI = weight/
height2

3. Checks if BMI is healthy (18.5 to 24.9) using comparison and logical operators
4. Prints formatted result

Enter weight ( kg ) : 70
2 Enter height ( m ) : 1.75
3 Your BMI : 22.86
4 Healthy : True
"""

print("=====BMI Calculator Program")

# st 1: get the weight of the user in kg

weight = float(input("Enter your weight in (kg): "))

# st 2: get the user height in meters

height = float(input("Enter your height in (meter): "))


# st 4: calculate the BMI of user

bmi = weight/(height** 2) 


# st 5: check the user's health using comparison operator

is_healthy = bmi >= 18.25  and bmi <= 24.9


# st 6: print the user's health

print(f"\nYour BMI : {bmi:.2f}\n")

print(f"\nYour health: {is_healthy}\n")
