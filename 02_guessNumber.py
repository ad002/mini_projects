#2 Guess the Number
#First: Generate a number unknown to user
#Second: User guess which number it is
#Third: Return whether guessed right or if not, whether
#guessed number too small or too high

#Hint: You'll need functions to check if user input is a actual number and if it
#is in the range of the to-guess-numbers

#Note: I also inserted a tryagain() method to aks user whether to play on after
#the first wrong guess. As I'm getting into Object Oriented Programming with
#"Learn Python the hard way" I tried to at least avoid some redundance by
#creating methods like guess() and tryagain() for some code consuming steps.


#First: Generate a random number
import random

#Generate a random number from Zero to 100 inclusive
randInt = random.randrange(101)
print("I've generated a random number between 0 and 100. Please guess")

#Second: User guesses number and third: Check whether right or wrong
def guess():
    #Take the guess, transform string input to int
    Userguess = int(input("Give me a number: "))

    #We need to check whether the user gives correct input
    #if he gives a too high or to small input (out of range), ask him
    #to give an input again, meaning: Call the guess function again.
    if Userguess>100 or Userguess <0:
        print("Your input should be between 0 and 100. Please try again")
        guess()
    #Check whether User hit the value
    if Userguess == randInt:
        #Chance of 1% is only true when first guess is right guess, but I
        #neglect to count the number of guesses, so I comment it out.
        #print("You won, although your chance was only 1%! Nice!")

        print("You won, congratulations!")
    #If too high, tell User and ask whether to play on
    elif Userguess>randInt:
        print("Your guess was too high.")
        tryagain()
    #If too small, tell User and ask whether to play on
    elif Userguess<randInt:
        print("Your guess was too low")
        tryagain()

#Outsorce the try again part to not repeat it inside the elif parts of "guess"
#Function
def tryagain():
    yesno= input("Do you want to try again? (Y/N)")
    #Call the Guess function again if he wants to play on
    if yesno=="Y" or yesno =="y":
        guess()
    #Exit the programm if he doesn't want to play on
    elif yesno=="N" or yesno =="n":
        exit()

    #If the user doesn's anwer correctly with y or n, repeat process/aks again
    else:
        print("Sorry, please answer if you want to play again by typing y or n")
        tryagain()


#Now we just have to call the guess function
guess()

#For right now we life in the perfect world that user inputs a number between
#our range of 0 and 100. We have to check whether input is right
