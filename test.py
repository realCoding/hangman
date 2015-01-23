__author__ = 'user'

import hangman

wordList = 'abc def ghy'.split()
word = hangman.getRandomWord(wordList)

print(word)