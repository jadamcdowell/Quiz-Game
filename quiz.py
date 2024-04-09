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

# variables to keep track of how many questions are correct and incorrect
correct = 0
incorrect = 0

# continue if correct number is entered for num of questions

# if 1 was entered for number of questions
if questions == 1:
    answer1 = input("\nWhat is 5 x 5? ")
    if answer1 == "25":
        print("Correct!")

        # keep track of correct answers
        correct += 1
    else:
        print("Incorrect! :(")

        # keep track of incorrect answers
        incorrect += 1


# if 2 was entered for number of questions
if questions == 2:
    answer1 = input("\nWhat is 30 x 30? ")
    if answer1 == "900":
        print("Correct!")

        # keep track of correct answers
        correct += 1
    else:
        print("Incorrect! :(")

        # keep track of incorrect answers
        incorrect += 1

    answer2 = input("\nWhat is the largest continent? ")
    if answer2 == "Asia":
        print("Correct!")

        # keep track of correct answers
        correct += 1
    else:
        print("Incorrect! :(")

        # keep track of incorrect answers
        incorrect += 1


# if 3 was entered for number of questions
if questions == 3:
    answer1 = input("\nWhat is the largest planet in the solar system? ")
    if answer1 == "Jupiter":
        print("Correct!")

        # keep track of correct answers
        correct += 1
    else:
        print("Incorrect! :(")

        # keep track of incorrect answers
        incorrect += 1

    answer2 = input("\nWhat is the chemical symbol for water? ")
    if answer2 == "H20":
        print("Correct!")

        # keep track of correct answers
        correct += 1
    else:
        print("Incorrect! :(")

        # keep track of incorrect answers
        incorrect += 1

    answer3 = input("\nWhat is the 81 divide 9? ")
    if answer3 == "9":
        print("Correct!")

        # keep track of correct answers
        correct += 1
    else:
        print("Incorrect! :(")

        # keep track of incorrect answers
        incorrect += 1
