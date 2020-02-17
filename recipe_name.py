# Get's recipe name and checks it is not blank

# Not Blank function goes here


def not_blank(question):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print(error)
        else:
            return response


# Main Routine goes here

error = "Your recipe has a error. Retry this statement."
has_errors = ""

recipe_name = not_blank("What is the recipe name? ")

print("No errors found. Creating Recipe...")
print("Recipe complete. Printing to console...")
print("You are making {}".format(recipe_name))

