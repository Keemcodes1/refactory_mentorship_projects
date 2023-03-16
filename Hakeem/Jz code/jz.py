
import random

number = random.randint(1, 10) # generate a random number between 1 and 10
guesses = 9 # set the number of guesses the user has
for i in range(guesses): # loop through the number of guesses
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("Congratulations! You guessed the number.")
        break # exit the loop if the user guesses correctly
    else:
        print("That's not the number.")
else:
    print("Sorry, you ran out of" )
#Guessing game project presentation