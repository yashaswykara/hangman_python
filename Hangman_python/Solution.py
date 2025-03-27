import random

stages=['''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
    ==========
    ''' ,'''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
    ==========
    '''  ,'''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
    ==========
    ''' ,'''
        +---+
        |   |
        O   |
       /|   |
            |
            |
    ==========
    ''' ,'''
        +---+
        |   |
        O   |
        |   |
            |
            |
    ==========
    ''' ,'''
        +---+
        |   |
        O   |
            |
            |
            |
    ==========
    ''' ,'''
        +---+
        |   |
            |
            |
            |
            |
    ==========
    ''' 
]
word_list=["aardvark","baboon","camel"]

#to keep track of how many lives are left
lives=6

#randomly choose a word fromt the word_list and assign it to a variable n then print it

chosen=random.choice(word_list)
print(chosen)

#ask the user to guess a letter and assign their answer to a variable called guess,make guess in lowercase

#create a placeholder with the same number of blanks as the chosen_word
placeholder = ""
word_length=len(chosen)
for position in range(word_length):
    placeholder+="_"
print(placeholder)

#use while loop to let the user guess again
game_over=False
correct_letters=[]


while not game_over:
    guess=input("Guess a letter: ").lower()

    #display that puts the guess letter in the right position and _ in the rest of the string

    display=""



    #check if the letter the user guessed is one of the letters in chosen.print "Right" if it is,else "Wrong"
    for letter in chosen:
        if letter==guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter   
        else:
            display+="_"

    print(display)

    if guess not in chosen:
        lives-=1
        if lives==0:
            game_over=True
            print("you lose")

    if "_"not in display:
        game_over=True
        print("You win")

    print(stages[lives])