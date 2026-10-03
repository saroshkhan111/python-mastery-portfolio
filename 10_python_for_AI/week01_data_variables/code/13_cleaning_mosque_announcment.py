"""
A mosque announcement is stored messily as:
announcement = " Jummah prayer at 1:30 PM "
Using string methods, remove the extra leading/trailing spaces and convert the text to uppercase.
Print the cleaned result.
"""

# Remove extra leading/trailing spaces and convert to uppercase
announcement = "    Jummah prayer at 1:30 PM     ".strip().upper()
print("\n",announcement,"\n")

