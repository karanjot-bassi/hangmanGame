#Karanjot Bassi - 30094007
#CPSC 231 - TUT 03
#Assignment 3 - Hangman

from fileinput import close     #Import all the neccacary libraries, random so that a secret word can be selected and turtle to draw hangman visual
import random
import turtle
WIDTH = 800 #Constants set for the window size of the turtle 
HEIGHT = 600

#Create the turtle and hangman stand.
pen = turtle.Turtle()
screen = turtle.getscreen()
screen.bgcolor("cyan")
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
pen.hideturtle()
pen.up()
pen.goto(100, 200)
pen.down()
pen.goto(200, 200)
pen.up()
pen.goto(150, 200)
pen.down()
pen.goto(150, 500)
pen.goto(400, 500)
pen.goto(400, 450)
pen.up()

# def a function to open and read the txt file and store each word into a list, also stripping the \n from each line, returning the list of words 
def readFile(file):
    txtFile = open(file, "r")
    data = txtFile.readlines()
    new_list = []
    for i in data:
        new_list.append(i.strip())
    txtFile = close()
    return new_list

# def function to select a random word, using the random library it will select a random word from the list but will only return thew word if the len is 4 or more 
def chooseSecretWord(data):
    word = random.choice(data)
    while len(word) < 4:
        word = random.choice(data)
    return word

# The following functions are made to draw sepreate parts of the hangman body, each names according to the body part, depending on user 
# try count each will be called accorinding 
def hangmanHead():
    pen.down()
    pen.color("blue")
    pen.circle(-25)
    pen.up()
def hangmanBody():
    pen.goto(400, 400)
    pen.down()
    pen.goto(400, 300)
    pen.up()
def hangmanLeftArm():
    pen.goto(400, 370)
    pen.down()
    pen.goto(350, 420)
    pen.up()
def hangmanRightArm():
    pen.goto(400, 370)
    pen.down()
    pen.goto(450, 420)
    pen.up()
def hangmanLeftLeg():
    pen.goto(400, 300)
    pen.down()
    pen.goto(350, 220)
    pen.up()
def hangmanRightLeg():
    pen.goto(400, 300)
    pen.down()
    pen.goto(450, 220)
    pen.up()
def hangmanLeftEye():
    pen.goto(390, 430)
    pen.down()
    pen.dot(5, "red")
    pen.up()
def hangmanRightEye():
    pen.goto(410, 430)
    pen.down()
    pen.dot(5, "red")
    pen.up()

# def the function that will play the hangman game, the function takes in the parameter and will not return anything but will tell user if they win or loose. 
def gamePlay(word):
    secret_word = list(word)        #store secret word as a list to make it easier to put the guessed letters in the correct position
    guess_length = "_" * len(word)  
    guess = list(guess_length)      #store each "_" as a list which will make it easier to replace with the correct letters
    tries = 8
    bad_guesses = []
    good_guesses = []

    while secret_word != guess and tries > 0:   #while the user does not find the word or the tries do not run out the loop will countinue
        count = 0   # Have count reset each guess, this will help with the index position 
        print("\nThe secret word looks like:", *guess)
        if len(bad_guesses) > 0:
            print("Your bad guesses so far:", *bad_guesses)
        print("You have", tries, "guess remaining")

        x = input("What is your Guess? ")
        
        if x in good_guesses or x in bad_guesses:
            print("You have already guessed", x, "try a different letter.\n")


        if x in word and x not in good_guesses:     #if the guessed letter is in the word, we loop through secret words, the guess will go through each index and if it is equal "_" in guess will be replaced with x(guessed letter)
            print("Nice Guess!\n")
            for i in secret_word:
                if x == i:
                    guess[count] = x
                    good_guesses.append(x)
                    count += 1
                else:
                    count += 1
        
        if x not in word and x not in bad_guesses:  #if x is not in the word we subract a try 
            print("Sorry, there is no", x, "\n")
            bad_guesses.append(x)
            tries -= 1
        if tries == 7:      #As try count decreases function for hangman body parts will be drawn
            hangmanHead()
        if tries == 6:
            hangmanBody()
        if tries == 5:
            hangmanLeftArm()
        if tries == 4:
            hangmanRightArm()
        if tries == 3:
            hangmanLeftLeg()
        if tries == 2:
            hangmanRightLeg()
        if tries == 1:
            hangmanLeftEye()
        if tries == 0:
            hangmanRightEye()

    if secret_word == guess and tries > 0:      #Once the loop is broken we check if the secret word and the guess are equal and that the tries stayed over zero, if this is true, user wins. Else game over
        print("Congratulations!")
        print("You guessed the secret word:", word)
    else:
        print("Game Over, the secret word was", word)


# def main function with no parameters but will run the above functions, and will have nothing to return
def main():
    mainFile = "/Users/karanjotbassi/Documents/School stuff/CPSC 231/Assignment #3/cpsc231-lexicon.txt"
    data = readFile(mainFile)
    secretWord = chooseSecretWord(data)
    gamePlay(secretWord)

#run the main function and play hangman 
main()
turtle.done()   #Close turtle window when user decides 
