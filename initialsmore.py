"""
This program will get the initials from a name given by the user, regardless
of how many spaces the user puts in the name.
Coded by Justin Le
"""

# Asks the user for their name, strips the spaces out and sets variable initials to the first letter of
# the name
name = str(input("Enter your name: "))
name = name.strip()
initials = name[0]

# Checks each letter of the name and if the current letter is a space and the
# next letter is not a space, the next letter is added to variable initials
for i in range(len(name)):
    if name[i] == " " and name[i+1] == " ":
        i = i + 1
        continue
    elif name[i] == " " and name[i+1] != " ":
        initials = initials + name[i+1]

# Capitalizes all letters in variable initials and prints it out
initials = initials.upper()
print("Initials: " + initials)
