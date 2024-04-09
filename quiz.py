print("Welcome to my computer quiz! ")

# Ask for users name
name = input("\nWhat is your name? ")

# Using users name, ask if they want to take a quiz
playing = input("\n" + name + ", do you want to take a quiz? ")

# if users answer is not "yes", quit
if playing != "yes":
    quit()

# if users answer is yes, display "Lets play"
print("\nLets play :)")

# initialize questions variable
questions = 0

# loop until valid input for answers is provided
while True:
    try:
        # prompt user for number of questions between 1 & 5
        questions = int(input("\nHow many questions do you want? (between 1 and 3) " ))

        # validate user input on questions
        if 1 <= questions <= 3:
            break
        else:
            # error message
            print("Sorry you have to choose between 1 and 3")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3")

