"""
THE % OPERATOR  (REMAINDER / MODULUS)

% means:  "What is LEFT OVER after I share?"
"""

# Example: the candy story
candies = 17
friends = 5

each_gets = candies // friends      # floor division: how many candies each friend gets
left_over = candies % friends       # modulus: what is LEFT OVER

print(each_gets)    # 3 candies
print(left_over)    # 2 candies left over
