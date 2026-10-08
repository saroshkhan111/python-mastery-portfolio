print("=================Grade Calculator Checker====================")
print("Enter Valid Number [1 - 100] or character 'A', 'B', 'C', 'D'\n")

marks = input("Enter Your Marks or Grade: ")

# 1. Agar user ne Letter enter kiya ho
if marks == "A":
    print("Student was absent")
elif marks == "B":
    print("Grade B")
elif marks == "C":
    print("Grade C")
elif marks == "D":
    print("Grade D")

# 2. Agar user ne Number (string) enter kiya ho
elif marks >= "90":
    print("Grade A")
elif marks >= "70":
    print("Grade B")
elif marks >= "50":
    print("Grade C")
elif marks >= "40":
    print("Fail")
else:
    print("Grade D / Below 40")

print("\n===========================Thanks for using check grade Program==========================")