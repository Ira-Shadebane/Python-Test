# Iterates through string...

# ask user for string

recipe_name = input("What is the recipe name? ")

error = "Your recipe name has numbers, which are not allowed. please repeat without numbers."
has_errors = ""

# look at each character in string and if it is a number, complain
for letter in recipe_name:
    if letter.isdigit() == True:
        print(error)
        has_errors = "yes"
        break

# give user feedback...
if has_errors != "yes":
    print("No errors found. Continue.")