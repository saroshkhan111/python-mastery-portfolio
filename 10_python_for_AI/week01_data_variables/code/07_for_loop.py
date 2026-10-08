# Problem Statement:
#Write a nested loop that prints all pairs of numbers where:
# The first number goes from 1 to 3
# The second number goes from 1 to 2

# Expected output:
#(1, 1)
#(1, 2)
#(2, 1)
#(2, 2)
#(3, 1)
#(3, 2)



# step 1: create the outer loop for the first range -> 1 to 3
for i in range(1, 4): 
    # step 2: create the inner loop for the second range -> 1 to 2
    for j in range(1, 3):
        print(i, j)  # print the current pair of numbers


# Dry Run
# 1 1     <-- i=1, j=1
# 1 2     <-- i=1, j=2
# 2 1     <-- i=2, j=1
# 2 2     <-- i=2, j=2
# 3 1     <-- i=3, j=1
# 3 2     <-- i=3, j=2