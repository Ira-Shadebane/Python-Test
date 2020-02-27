# Get's recipe name and checks it is not blank

recipe_name = input("What is the recipe name? ")

error = "Your recipe name has numbers, which are not allowed. please repeat without numbers."
has_errors = ""

# Not Blank function goes here
def not_blank(question):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print(error)
        else:
            return response

        # look at each character in string and if it is a number, complain
        for letter in recipe_name:
            if letter.isdigit() == True:
                print(error)
                has_errors = "yes"
                break
            # give user feedback...
            if has_errors != "yes":
                print("No errors found. Continue.")

# Main Routine goes here

error = "Your recipe has errors. Retry this statement."
has_errors = ""

recipe_name = not_blank("What is the recipe name? ")

print("No errors found. Creating Recipe...")
print("Recipe complete. Printing to console...")
print("You are making {}".format(recipe_name))

