import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    b=1
    for i in secret_word:
        if i in letters_guessed:
            b=1*b
        else:
            b=0
    if b == 1:
        return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    Glist = ['_', ' '] * len(secret_word)
    Glist.pop()
    for (index, letter) in enumerate(secret_word):
        if letter in letters_guessed:
            Glist[2*index] = letter
    Gstr = ''
    for elem in Glist:
        Gstr = Gstr + elem
    return Gstr

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    astr=''
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i not in letters_guessed:
            astr= astr+i
    return astr
    


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('''\nThis word contains %d character(s).''' % (len(secret_word)))
    print('''You start with 6 guesses\n''')
    guesses = 6
    letters_guessed=[]
    while guesses >0:
        print('You have %d guess(es) remaining.' % (guesses))
        print('''Unguessed letters: %s\n''' % (get_available_letters(letters_guessed)))
        
        inp = input('Guess one letter: ')
        if inp.isalpha():
            inp = inp.lower()
        else:
            print('''You can only write in an alphabet.''')
            continue
        if len(inp)==1:
            if inp in get_available_letters(letters_guessed):
                letters_guessed.append(inp)
            else:
                print('''You already guessed the same letter!\n''')
                continue
        else:
            print('''Enter just 1 letter!\n''')
            continue
        if is_word_guessed(secret_word, letters_guessed):
            print('''So far you got: %s\n\n\n''' % (get_guessed_word(secret_word,letters_guessed)))
            print('Congratulations!')
            print('The word was %s.' % (secret_word))
            break
        else:
            if inp not in secret_word:
                print("""Sorry, '%s' is not in the word.\n""" % (inp))
                guesses -= 1
            else:
                print("""Good job, '%s is in the word.\n""" % (inp))
            print('''So far you got: %s\n\n\n''' % (get_guessed_word(secret_word,letters_guessed)))
        
        # feedback
        



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if len(my_word) != 2* len(other_word) -1:
        return False
    else:
        boolean = 1
        for (index, letter) in enumerate(my_word):
            if index%2 ==0:
                if letter == '_' or letter == other_word[int(index/2)]:
                    boolean = boolean * 1
                else:
                    boolean = boolean * 0
        return boolean == 1

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for word in wordlist:
        if match_with_gaps(my_word, word):
            spaceindices = []
            for (index, letter) in enumerate(my_word):
                if index % 2 ==0 :
                    if letter == '_':
                        spaceindices.append(int(index/2))
            boolean = 1
            for index in spaceindices:
                if word[index] not in my_word:
                    boolean = 1 * boolean
                else:
                    boolean = 0 * boolean
            if boolean == 1:
                print(word)



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('''\nThis word contains %d character(s).''' % (len(secret_word)))
    print('''You start with 6 guesses and if you press " * ", you can get a hint.\n''')
    guesses = 6
    letters_guessed=[]
    while guesses >0:
        print('You have %d guess(es) remaining.' % (guesses))
        print('''Unguessed letters: %s\n''' % (get_available_letters(letters_guessed)))
        inp = input('Guess one letter: ')
        if inp.isalpha():
            inp = inp.lower()
        elif inp != '*':
            print("""You can only write in an alphabet or an ' * '.\n""")
            continue
        
        if len(inp)==1:
            if inp == '*':                
                print('''\nThese are the possible words:''')
                g = get_guessed_word(secret_word,letters_guessed)
                show_possible_matches(g)
                guesses -= 1
                if guesses == 0:
                    print("You've failed. The answer is %s" % (secret_word))
                    break
                continue
            elif inp in get_available_letters(letters_guessed):
                letters_guessed.append(inp)
            else:
                print('''You already guessed the same letter!\n''')
                continue
        else:
            print('''Enter just 1 letter!\n''')
            continue
        if is_word_guessed(secret_word, letters_guessed):
            print('''So far you got: %s\n\n\n''' % (get_guessed_word(secret_word,letters_guessed)))
            print('Congratulations!')
            print('The word was %s.' % (secret_word))
            break
        else:
            if inp not in secret_word:
                print("""Sorry, '%s' is not in the word.\n""" % (inp))
                guesses -= 1
                if guesses == 0:
                    print("You've failed. The answer is %s" % (secret_word))
                    break
            else:
                
                print("""Good job, '%s is in the word.\n""" % (inp))
            print('''So far you got: %s\n\n\n''' % (get_guessed_word(secret_word,letters_guessed)))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)


