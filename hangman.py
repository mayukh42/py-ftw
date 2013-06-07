# hangman.py
# dependency: words.txt
'''
command line implementation of the famous word puzzle game
TODO: 2D graphics for the hangman
'''

from random import randrange

MAX_GUESSES = 6

def load_words():
    print "Loading word list from file..."
    inp = open("words.txt", 'r')
    line = inp.readline() # all words in one BIG line!
    wordlist = line.split()
    print '     ', len(wordlist), "words loaded."
    inp.close()
    return wordlist

words_dict = load_words()

def get_word():
    return words_dict[randrange(0,len(words_dict))]

def char_pos_map(word):
    letters_guessed = dict(zip(word, [[] for i in range(len(word))]))
    for i in range(len(word)):
        letters_guessed[word[i]].append(i)
    return letters_guessed

def play_hangman():
    # run a loop while mistakes are less than allowed limit, and at every correct guess, fill the corresponding slots. note that strings are immutable, so use a char list for building the guessed word. at the start, give number of chars in the secret word as hint.
    mistakes = 0
    secret_word = get_word()
    print 'the secret word has', len(secret_word), 'letters'
    letters_guessed = char_pos_map(secret_word)
    guessedsofar = ['_' for i in range(len(secret_word))]

    while mistakes < MAX_GUESSES:
        print 'word built so far:', ''.join(guessedsofar), 'mistakes:', mistakes 
        c = raw_input('enter your guess: ')
        if c not in secret_word:
            mistakes += 1
        else:
            pos = letters_guessed[c]
            repeat = False
            for i in pos:
                if guessedsofar[i] == '_':
                    guessedsofar[i] = c
                else:
                    repeat = True
            if repeat:
                mistakes += 1
        if ''.join(guessedsofar) == secret_word:
            print 'the secret word is ', secret_word
            return 'you won!'
    # show the word even if player lost
    print 'the secret word is ', secret_word
    return 'you are hanged!'


def main():
    # usage: $ python hangman.py
    print play_hangman()


if __name__ == '__main__':
    main()
