"""
Problem 1
Please read the Hangman Introduction before starting this problem. 
We'll start by writing 3 simple functions that will help us easily code the Hangman problem. 
First, implement the function isWordGuessed that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. 
This function returns a boolean - True if secretWord has been guessed (ie, all the letters of secretWord are in lettersGuessed) and False otherwise.

Example Usage:

    secretWord = 'apple' 
    lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    print(isWordGuessed(secretWord, lettersGuessed))
    False

For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.
"""
print(" ")
print("This is Problem 1: ")
def isWordGuessed(secretWord, lettersGuessed):
    
    for i in lettersGuessed:
        
        if i  not in secretWord:
            
            return False

    return True

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))
print(" ")


"""
Problem 2
Next, implement the function getGuessedWord that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. 
This function returns a string that is comprised of letters and underscores, based on what letters in lettersGuessed are in secretWord. 
This shouldn't be too different from isWordGuessed!

Example Usage:

    secretWord = 'apple' 
    lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    print(getGuessedWord(secretWord, lettersGuessed))
    '_ pp_ e'

When inserting underscores into your string, it's a good idea to add at least a space after each one, 
so it's clear to the user how many unguessed letters are left in the string (compare the readability of ____ with _ _ _ _ ). 
This is called usability - it's very important, when programming, to consider the usability of your program. 
If users find your program difficult to understand or operate, they won't use it!

For this problem, you are free to use spacing in any way you wish - our grader will only check that the letters and underscores are in the proper order; 
it will not look at spacing. We do encourage you to think about usability when designing.

For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.
"""

print("This is Problem 2: ")

def getGuessedWord(secretWord, lettersGuessed):

    ans = str()
    for i in secretWord:
        
        if i in lettersGuessed:
           
            ans += i
        
        else:
           
            ans += "_"
  
    return ans

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))
print(" ")

"""
Problem 3
Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. 
This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are not in lettersGuessed.

Example Usage:

    lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    print(getAvailableLetters(lettersGuessed))
    abcdfghjlmnoqtuvwxyz

Note that this function should return the letters in alphabetical order, as in the example above.

For this function, you may assume that all the letters in lettersGuessed are lowercase.

Hint: You might consider using string.ascii_lowercase, which is a string comprised of all lowercase letters:

    import string
    print(string.ascii_lowercase)
abcdefghijklmnopqrstuvwxyz
"""

import string
print("This is Problem 3: ")

def getAvailableLetters(lettersGuessed):

    ans = str()
    for i in string.ascii_lowercase:
       
        if i not in lettersGuessed:
           
            ans += i
    
    return ans

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
print(" ")

"""
Problem 4
Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. 
This starts up an interactive game of Hangman between the user and the computer. 
Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.

Hints:
You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py) to load the words and pick a random one. 
Note that the functions loadWords and chooseWord should only be used on your local machine, not in the tutor. 
When you enter in your solution in the tutor, you only need to give your hangman function.

Consider using lower() to convert user input to lower case. For example:

guess = 'A'
guessInLowerCase = guess.lower()
Consider writing additional helper functions if you need them!

There are four important pieces of information you may wish to store:

secretWord: The word to guess.
lettersGuessed: The letters that have been guessed so far.
mistakesMade: The number of incorrect guesses made so far.
availableLetters: The letters that may still be guessed. 
Every time a player guesses a letter, the guessed letter must be removed from 
availableLetters (and if they guess a letter that is not in availableLetters, you should print a message telling them they've already guessed that - so try again!).

Sample Output
The output of a winning game should look like this...
	Loading word list from file...
	55900 words loaded.
	Welcome to the game, Hangman!
	I am thinking of a word that is 4 letters long.
	-------------
	You have 8 guesses left.
	Available letters: abcdefghijklmnopqrstuvwxyz
	Please guess a letter: a
	Good guess: _ a_ _
	------------
	You have 8 guesses left.
	Available letters: bcdefghijklmnopqrstuvwxyz
	Please guess a letter: a
	Oops! You've already guessed that letter: _ a_ _
	------------
	You have 8 guesses left.
	Available letters: bcdefghijklmnopqrstuvwxyz
	Please guess a letter: s
	Oops! That letter is not in my word: _ a_ _
	------------
	You have 7 guesses left.
	Available letters: bcdefghijklmnopqrtuvwxyz
	Please guess a letter: t
	Good guess: ta_ t
	------------
	You have 7 guesses left.
	Available letters: bcdefghijklmnopqruvwxyz
	Please guess a letter: r
	Oops! That letter is not in my word: ta_ t
	------------
	You have 6 guesses left.
	Available letters: bcdefghijklmnopquvwxyz
	Please guess a letter: m
	Oops! That letter is not in my word: ta_ t
	------------
	You have 5 guesses left.
	Available letters: bcdefghijklnopquvwxyz
	Please guess a letter: c
	Good guess: tact
	------------
	Congratulations, you won!
          
And the output of a losing game should look like this...
	Loading word list from file...
	55900 words loaded.
	Welcome to the game Hangman!
	I am thinking of a word that is 4 letters long.
	-----------
	You have 8 guesses left.
	Available Letters: abcdefghijklmnopqrstuvwxyz
	Please guess a letter: a
	Oops! That letter is not in my word: _ _ _ _
	-----------
	You have 7 guesses left.
	Available Letters: bcdefghijklmnopqrstuvwxyz
	Please guess a letter: b
	Oops! That letter is not in my word: _ _ _ _
	-----------
	You have 6 guesses left.
	Available Letters: cdefghijklmnopqrstuvwxyz
	Please guess a letter: c
	Oops! That letter is not in my word: _ _ _ _
	-----------
	You have 5 guesses left.
	Available Letters: defghijklmnopqrstuvwxyz
	Please guess a letter: d
	Oops! That letter is not in my word: _ _ _ _
	-----------
	You have 4 guesses left.
	Available Letters: efghijklmnopqrstuvwxyz
	Please guess a letter: e
	Good guess: e_ _ e
	-----------
	You have 4 guesses left.
	Available Letters: fghijklmnopqrstuvwxyz
	Please guess a letter: f
	Oops! That letter is not in my word: e_ _ e
	-----------
	You have 3 guesses left.
	Available Letters: ghijklmnopqrstuvwxyz
	Please guess a letter: g
	Oops! That letter is not in my word: e_ _ e
	-----------
	You have 2 guesses left.
	Available Letters: hijklmnopqrstuvwxyz
	Please guess a letter: h
	Oops! That letter is not in my word: e_ _ e
	-----------
	You have 1 guesses left.
	Available Letters: ijklmnopqrstuvwxyz
	Please guess a letter: i
	Oops! That letter is not in my word: e_ _ e
	-----------
	Sorry, you ran out of guesses. The word was else. 
          

Note that if you choose to use the helper functions isWordGuessed, getGuessedWord, or getAvailableLetters, you do not need to paste your definitions in the box. 
We have supplied our implementations of these functions for your use in this part of the problem. 
If you use additional helper functions, you will need to paste those definitions here.

Your function should include calls to input to get the user's guess.
"""
print("This is Problem 4: ")
def hangman(secretWord):

    print("Loading word list from file...")
    print("55900 words loaded. ")
    print("Welcome to the game, Hangman!")

    secWordLength = len(secretWord)

    print("I am thinking of a word that is " + str(secWordLength) + " letters long.")

    print("------------")

    lettersGuessed = []
    mistakesMade = 0
    availableLetters = string.ascii_lowercase
    availableGuesses = 8
    done = False

    while(done == False):

        print("You have " + str(availableGuesses) + " guesses left.")
        print("Available Letters: " + str(availableLetters))
        user_input = input("Please guess a letter: ")

        if user_input not in getAvailableLetters(lettersGuessed):
            print("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)))
        
        elif user_input not in secretWord:
            lettersGuessed += user_input
            availableLetters = getAvailableLetters(lettersGuessed)
            availableGuesses -= 1
            print("Oops! That letter is not in my word: " + str(getGuessedWord(secretWord, lettersGuessed)))
        
        elif user_input in secretWord:
            
            lettersGuessed += user_input
            availableLetters = getAvailableLetters(lettersGuessed)
            print("Good guess: " + str(getGuessedWord(secretWord, lettersGuessed)))
        
        print("------------")

        if getGuessedWord(secretWord, lettersGuessed) == secretWord or availableGuesses == 0:
            done = True
    
    if availableGuesses == 0:
        print("Sorry, you ran out of guesses. The word was " + str(secretWord) + ".")
    
    if getGuessedWord(secretWord, lettersGuessed) == secretWord:
        print("Congratulations, you won!")
    
    print(" ")

hangman('tact')



