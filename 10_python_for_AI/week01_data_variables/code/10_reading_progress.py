"""
Problem Statement:
A student has read 145 pages out of a 604-page Qur’an. Using an f-string, print a sentence showing
the percentage completed, rounded to 2 decimal places, in the form: "You have completed % of
the Qur’an."
"""

# step 1: Print the header
print("\n" + "=" * 50)
print("         Reading Progress ")
print("=" * 50)

# step 2: create two variables for total_pages and read_pages
total_pages = 604
read_pages = 145

# step 3: calculate the percentage completed
percentage = (read_pages / total_pages) * 100


print()
# step 4: print the percentage completed
print(f"You have completed {percentage:.2f}% of the Quran\n")