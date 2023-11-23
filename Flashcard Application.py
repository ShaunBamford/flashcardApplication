# Importing required libaries
from random import choice
# Storing our flashcards
flashcard = {

    'Example Flashcard Question':'example flashcard answer'

}

# Defining our quiz function
def quiz():
    # Preparing our loop to keep program running if user wishes so
    flag = True
    while flag == True:
        # Picking a random question to ask the user
        question, answer = choice(list(flashcard.items()))
        # Asks user the question, .format adds it to the print statement
        print("{}".format(question))
        # User inputs answer
        userAnswer = input("> ")
        # Checking user answer
        if userAnswer.lower() == answer:
            print("\nThat is correct, the answer is {}".format(answer),"\n")
        else:
            print("\nWrong answer, the answer is {}".format(answer),"\n")
        
        # Preparing our loop to check user input
        Flag = True

        while Flag == True:
            option = input("Press 0 if you want to play again\n> ")
            # Checks if user inputs an integer, if so proceed else ask again
            try:
                int(option)
                Flag = False
            except:
                print("Invalid option, try again\n")

        # Checks if the user wants to play again (0 means play again)
        if option == '0':
            flag = True
        else:
            flag = False
# Calling our function
quiz()