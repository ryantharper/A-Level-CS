# Hangman ~~ Ryan Harper

from random import choice
from getpass import getpass

# To play Player VS Player, it is recommended that you launch
# this from the command line or from inside the File Explorer.


hangman = ["-------\n   |  |\n   0  |\n      |\n      |\n      |\n      |\n______|",
      "-------\n   |  |\n   0  |\n \_|_/|\n      |\n      |\n      |\n______|",
      "-------\n   |  |\n   0  |\n \_|_/|\n   |  |\n      |\n      |\n______|",
      "-------\n   |  |\n   0  |\n \_|_/|\n   |  |\n  / \ |\n      |\n______|",
      "-------\n   |  |\n   0  |\n \_|_/|\n   |  |\n  / \ |\n d   b|\n______|"]

# Main Game Function
def game(secret):
    guesses = "" # Initialises guesses

    incorrect = 0 # Initialises incorrect value

    while incorrect < 5:
        guess = str(input("Guess a letter:"))
        guesses += guess
        # If what the player entered is not in the word
        if guess not in secret:
            # Print out the hangman, according to how many incorrect answers the users has entered
            for x in range(incorrect+1):
                print(hangman[x])
            incorrect+=1 # Increment incorrect
        # If what the player did enter is in the word
        else:
            # Print out word, showing any guessed letters
            for letter in secret: 
                if letter in guesses:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")
        print("Guesses: " + guesses + "\n") # Tells user what letters they have guessed

        # If the user has correctly guessed (all spaces are filled)
        if all(l in guesses for l in secret) == True: 
            print("Congratulations! You Won!")
            break
    # Player loses
    if incorrect == 5:
        print("The correct answer was " + secret)
        
    # Prevents immediate shutdown on command prompt
    k = input("Press Close To Exit")

# Player Vs AI function
def pvAI():
    print("Time to play Hangman VS COMPUTER!")
    items = ["crocodile", "tiger", "lion", "koala"]

    #Chooses item from list 'items'
    secret = choice(items)
    game(secret)

#Player vs Player function
def pvp():
    print("Time to play Hangman, 2 player!")
    # getpass hides what the user enters, prevents cheating
    secret = getpass("PLAYER, ENTER WORD FOR THE OTHER PERSON TO GUESS: ")
    game(secret)
    

print("HANGMAN: Would you like to (1) Player VS Computer\n(2) Player VS Player \nIt is recommended to run (2) from the command line -- or directly launch it from File Explorer")
playerOp = int(input(">>> "))

if playerOp == 1:
    pvAI()
elif playerOp == 2:
    pvp()
else:
    print("Confused. Launching Player Vs AI as default")
    pvAI()
    

    
        

    
        
