"""
Problem Statement:
A student’s profile arrives as a single messy string:
profile = " Ayesha , 17 , Lahore "
Using .split(",") and string methods (such as .strip()), separate this into a name, age, and city.
Convert the age to an integer. Then print a clean profile card using an f-string in the form: "Name:
| Age: | City: "


Expected Output:
Name: Ayesha | Age: 17 | City: Lahore

"""

# step 1: create a variable and store the string messy profile in the string

messy_str = " Ayesha , 17 , Lahore "


# step 2: split the messy string using a split method
profile = messy_str.split(",")

# step 3: strip any extra whitespace from each element in the profile list


name = profile[0].strip()

age  = int(profile[1].strip())

city = profile[2].strip()

# step 4: print the clean profile card using an f - string
print(f"Name: {name} | Age: {age} | City: {city}")





