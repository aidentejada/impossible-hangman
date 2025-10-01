# Hangman (English Dictionary Edition)

I wrote this quick Hangman game on October 21, 2023. The gimmick: it pulls from the entire NLTK English words corpus (~236k words), so you’ll get everything from common words to absolutely cursed dictionary entries. It’s a console game and I built it fast for fun.

## What it does
- Downloads the NLTK `words` corpus at runtime and loads a word list (~236k entries).
- Picks a random word, tells you its length, and gives you 7 guesses.
- You guess letters; correct letters fill into the positions, blanks stay as `_`.
- Clears the screen between steps for a little “choosing your word…” animation.
- You win when there are no underscores left; you lose when guesses hit 0 (then it shows the word).

## How to run
1. Make sure you have Python 3.8+ installed.
2. (First time) install NLTK:  
   pip install nltk
3. Run the script:  
   python hangman.py  
   The script itself runs `nltk.download('words')` the first time to fetch the dictionary.

## Notes
- This was a half-hour side project. It’s intentionally simple and leans on a long if/elif chain for multiple occurrences of a letter.
- The word list is huge; expect obscure words. That’s part of the joke.
- The screen clear uses os.system("cls"), which is Windows-only. On macOS/Linux you can either ignore the clears or change those lines to os.system("clear").
- Input is a single letter at a time; no validation beyond that.
- You have 7 total wrong guesses.

## Example session
Choosing your word...  
Word Chosen!  

Your word has 8 letters. Good Luck!!  
Guess a letter! --> e  
Correct!  
['_', 'e', '_', '_', '_', '_', '_', '_']

## Why I made it
I wanted a goofy Hangman that uses “every word in English” so it’s hilariously hard. Also a quick excuse to play with the NLTK words corpus.

## Possible improvements
- Replace the repeated elif blocks with a single loop over all matching positions.
- Add input validation and show previously guessed letters.
- Swap cls/clear depending on OS.
- Let players choose between “dictionary mode” and a smaller, normal word list.
