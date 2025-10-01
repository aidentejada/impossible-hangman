import random
import nltk
import sys
import os
from os import system
import time
nltk.download('words')
from nltk.corpus import words

### INITIALIZATIONS
length = 0
x = 0
word = []
list = []
wordlist = []
def setup():
    global length
    global x
    global word
    global list
    global wordlist
    wordlist = words.words() ##### Library of 236k words
    list = []
    word = wordlist[random.randint(0, len(wordlist) -1 )]
    x = 1
    while x < len(word):
        x= x+1
        list.append(word[-1+x])
    length = len(wordlist)


def game():
    global length
    global wordlist
    global word
    global text
    score = 7
    time.sleep(3)
    v = 0
    while v < 5:
        os.system("cls")
        print("Choosing your word")
        time.sleep(0.2)
        os.system("cls")
        print("Choosing your word.")
        time.sleep(0.2)
        os.system("cls")
        print("Choosing your word..")
        time.sleep(0.2)
        os.system("cls")
        print("Choosing your word...")
        time.sleep(0.2)
        v = v+1
    print()
    print("Word Chosen!")
    print()
    print("Your word has {} letters. Good Luck!!".format(len(word)))
    word = [*word]
    guesslist = []
    for letter in word:
        guesslist.append("_")
   
    while score > 0:
        guessletter = str(input("Guess a letter! --> "))
        print('')

        m = word.count(guessletter)
        if m == 1:
            positions = [index for index, value in enumerate(word) if value == guessletter]
            guesslist.pop(positions[0])
            guesslist.insert(positions[0], guessletter)
            print("Correct!")
            print(guesslist)
        elif m == 2:
            positions = [index for index, value in enumerate(word) if value == guessletter]
            guesslist.pop(positions[0])
            guesslist.insert(positions[0], guessletter)
            guesslist.pop(positions[1])
            guesslist.insert(positions[1], guessletter)
            print("Correct!")
            print(guesslist)
        elif m == 3:
            positions = [index for index, value in enumerate(word) if value == guessletter]
            guesslist.pop(positions[0])
            guesslist.insert(positions[0], guessletter)
            guesslist.pop(positions[1])
            guesslist.insert(positions[1], guessletter)
            guesslist.pop(positions[2])
            guesslist.insert(positions[2], guessletter)
            print("Correct!")
            print(guesslist)
        elif m == 4:
            positions = [index for index, value in enumerate(word) if value == guessletter]
            guesslist.pop(positions[0])
            guesslist.insert(positions[0], guessletter)
            guesslist.pop(positions[1])
            guesslist.insert(positions[1], guessletter)
            guesslist.pop(positions[2])
            guesslist.insert(positions[2], guessletter)
            guesslist.pop(positions[3])
            guesslist.insert(positions[3], guessletter)
            print("Correct!")
            print(guesslist)
        elif m == 5:
            positions = [index for index, value in enumerate(word) if value == guessletter]
            guesslist.pop(positions[0])
            guesslist.insert(positions[0], guessletter)
            guesslist.pop(positions[1])
            guesslist.insert(positions[1], guessletter)
            guesslist.pop(positions[2])
            guesslist.insert(positions[2], guessletter)
            guesslist.pop(positions[3])
            guesslist.insert(positions[3], guessletter)
            guesslist.pop(positions[4])
            guesslist.insert(positions[4], guessletter)
            print("Correct!")
            print(guesslist)
        elif m == 6:
            positions = [index for index, value in enumerate(word) if value == guessletter]
            guesslist.pop(positions[0])
            guesslist.insert(positions[0], guessletter)
            guesslist.pop(positions[1])
            guesslist.insert(positions[1], guessletter)
            guesslist.pop(positions[2])
            guesslist.insert(positions[2], guessletter)
            guesslist.pop(positions[3])
            guesslist.insert(positions[3], guessletter)
            guesslist.pop(positions[4])
            guesslist.insert(positions[4], guessletter)
            guesslist.pop(positions[5])
            guesslist.insert(positions[5], guessletter)
            print("Correct!")
            print(guesslist)
        elif m == 0:
            print("Incorrect!")
            score = score-1
            print("You have {} guesses left!".format(score))
            if score == 0:
                print("You lost! Try again!")
                print("Your word was {}".format(word))
            print()
        if guesslist.count("_") == 0:
            print("You beat the worlds hardest game of hangman!")
            score = 0

    print("Thanks for playing!")



setup()
game()
