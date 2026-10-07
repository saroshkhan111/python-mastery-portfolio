"""
Student Grade System:
Check if a student passed (marks ≥50). If passed,
check if marks are ≥80 to print "Distinction", else print "Passed". If failed,
print "Failed".
"""

# st 1: Print the header Student Grade Calculator
print()
print("=" * 50)
print("           Student Grade Calculator Program")
print("=" * 50)
print()


# st 2: Get the marks from the user
marks = float(input("Enter your marks: "))

# st 3: Apply Nested if / else for checking criteria
if marks >= 50:

    #st 4: Apply another nested if/else
    if marks >= 80:
        print("Distinction")
    else:
        print("Passed")    
else:
    print("Fail")
print()    