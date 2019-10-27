"""
This program will get the initials from a name given by the user.
Coded by Justin Le
"""

# Asks the user for their name and sets variable initials to the first letter of
# the name
name = str(input("Enter your name: "))
initials = name[0]

# Checks each letter of the name and if the current letter is a space, the
# letter after is added to variable initials
for i in range(len(name)):
    if name[i] == " ":
        initials = initials + name[i+1]

# Capitalizes all letters in variable initials and prints it out
initials = initials.upper()
print("Initials: " + initials)
