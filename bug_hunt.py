# BUG: Added the missing closing quote to fix the SyntaxError.
print("Welcome to the Bug Hunt!")

name = input("What is your name? ")

# BUG: Changed "nmae" to "name" so the user's name is displayed correctly.
print("Nice to meet you, " + name)

age = input("How old are you? ")

# BUG: Converted age to int before adding 1 because input() returns a string.
print("Next year you will be " + str(int(age) + 1))
