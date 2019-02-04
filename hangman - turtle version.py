import random
import string
import turtle
WORDLIST_FILENAME = "words.txt"
def head(t):
    t.penup()#head
    t.setposition(200,100)
    t.pendown()
    t.circle(50)#head done
    turtle.update()
def body(t):
    t.penup() #body
    t.setposition(200,100)
    t.pendown()
    t.setposition(200, -70)#body done
    turtle.update()
def larm(t):
    t.penup()#left arm
    t.setposition(200,100)
    t.pendown()
    t.setposition(125, 25)#left arm done
    turtle.update()
def rarm(t):
    t.penup()#right arm
    t.setposition(200,100)
    t.pendown()
    t.setposition(275, 25)#right arm done
    turtle.update()
def lleg(t):
    t.penup()#left leg
    t.setposition(200, -70)
    t.pendown()
    t.setposition(100,-250)#left leg done
    turtle.update()
def rleg(t):
    t.penup()#right leg
    t.setposition(200,-70)
    t.pendown()
    t.setposition(300,-250)#right leg done
    turtle.update()
def dead(word, t):
    t.penup()#dead face
    t.setposition(175,175)
    t.pendown()
    t.setposition(190, 160)
    t.penup()
    t.setposition(175, 160)
    t.pendown()
    t.setposition(190,175)
    t.penup()
    t.setposition(210,175)
    t.pendown()
    t.setposition(225,160)
    t.penup()
    t.setposition(210,160)
    t.pendown()
    t.setposition(225,175)#dead face done
    t.penup()
    t.setposition(-100,100)
    t.pendown()
    t.color('red')
    t.write('Game Over' , align='center', font=('Arial', 50, 'bold') )
    t.penup()
    t.setposition(-100,0)
    t.color('blue')
    t.write('Answer: %s' % (word), align='center', font=('Arial', 30, 'bold'))
    t.color('white')
    turtle.update()
def victory(word,t):
    t.penup()
    t.setposition(-90,0)
    t.pendown()
    t.color('yellow')
    t.write("Victory!\nYou're so genius\nOmg" , align='center', font=('Arial', 40, 'bold') )
    t.penup()
    t.setposition(-100,-50)
    t.color('blue')
    t.write('Answer: %s' %(word), align='center', font=('Arial', 30, 'bold'))
    t.color('white')
    turtle.update()
def blank(word,t):
    t.penup()
    t.setposition(-100,-100)
    t.pendown()
    if len(word) <= 27:
        t.write(word , align='center', font=('Arial', 30, 'bold') )
    else:
        t.write(word[:28] , align='center', font=('Arial', 30, 'bold') )
        t.penup()
        t.setposition(-100, -150)
        t.pendown()
        t.write(word[29:] , align='center', font=('Arial', 30, 'bold') )
    turtle.update()
def rest(word,t):
    new = ''
    for i in word:
        new = new + i.upper() + ' '
    new.rstrip()
    t.penup()
    t.setposition(-330,-200)
    t.pendown()
    t.write('Unguessed words:', align='left', font=('Arial', 15, 'bold') )
    t.penup()
    t.setposition(-320,-230)
    t.write(new, align='left', font=('Arial', 15, 'bold') )
    turtle.update()
def rem(num, t):
    t.penup()
    t.setposition(330,250)
    t.write('Remaining guesses: %d' % (num), align='right', font=('Arial', 15, 'bold') )
    turtle.update()
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
    astr=''
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i not in letters_guessed:
            astr= astr+i
    return astr
def hangman(secret_word):
    print('''\nThis word contains %d character(s).''' % (len(secret_word)))
    print('''You start with 6 guesses\n''')
    guesses = 6
    t3=turtle.Turtle()
    t3.ht()
    t3.color('white')
    t3.pensize(3)
    rem(guesses,t3)
    letters_guessed=[]
    t2=turtle.Turtle()
    t2.color('white')
    t2.ht()
    t2.pensize(3)
    blank(get_guessed_word(secret_word,letters_guessed),t2)
    t1=turtle.Turtle()
    t1.ht()
    t1.color('white')
    t1.pensize(3)
    rest(get_available_letters(letters_guessed),t1)
    while guesses >0:
        print('You have %d guess(es) remaining.' % (guesses))
        print('''Unguessed letters: %s\n''' % (get_available_letters(letters_guessed)))
        t1.clear()
        t1=turtle.Turtle()
        t1.color('white')
        t1.pensize(3)
        t1.ht()
        rest(get_available_letters(letters_guessed),t1)
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
            t2.clear()
            t2=turtle.Turtle()
            t2.color('white')
            t2.ht()
            t2.pensize(3)
            blank(get_guessed_word(secret_word,letters_guessed),t2)
            victory(secret_word, t)
            i=input('Press any key to continue.')
            t1.clear()
            t2.clear()
            t3.clear()
            t.clear()
            break
        else:
            if inp not in secret_word:
                print("""Sorry, '%s' is not in the word.\n""" % (inp))
                guesses -= 1
                t3.clear()
                t3=turtle.Turtle()
                t3.ht()
                t3.color('white')
                t3.pensize(3)
                rem(guesses,t3)
                if guesses == 5:
                    head(t)
                elif guesses == 4:
                    body(t)
                elif guesses == 3:
                    larm(t)
                elif guesses == 2:
                    rarm(t)
                elif guesses == 1:
                    lleg(t)
                elif guesses == 0:
                    print("You've failed. The answer is %s" % (secret_word))
                    rleg(t)
                    dead(secret_word,t)
                    i=input('Press any key to continue.')
                    t1.clear()
                    t2.clear()
                    t3.clear()
                    t.clear()
                    break
            else:
                print("""Good job, '%s is in the word.\n""" % (inp))
            print('''So far you got: %s\n\n\n''' % (get_guessed_word(secret_word,letters_guessed)))
            t2.clear()
            t2=turtle.Turtle()
            t2.color('white')
            t2.ht()
            t2.pensize(3)
            blank(get_guessed_word(secret_word,letters_guessed),t2)
def match_with_gaps(my_word, other_word):
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
def show_possible_matches(my_word, letters_guessed):
    for word in wordlist:
        if match_with_gaps(my_word, word):
            spaceindices = []
            for (index, letter) in enumerate(my_word):
                if index % 2 ==0 :
                    if letter == '_':
                        spaceindices.append(int(index/2))
            boolean = 1
            for index in spaceindices:
                if word[index] not in my_word and word[index] in get_available_letters(letters_guessed):
                    boolean = 1 * boolean
                else:
                    boolean = 0 * boolean
            if boolean == 1:
                print(word)
def hangman_with_hints(secret_word):
    print('''\nThis word contains %d character(s).''' % (len(secret_word)))
    print('''You start with 6 guesses and if you press " * ", you can get a hint.\n''')
    guesses = 6
    t3=turtle.Turtle()
    t3.ht()
    t3.color('white')
    t3.pensize(3)
    rem(guesses,t3)
    letters_guessed=[]
    t2=turtle.Turtle()
    t2.color('white')
    t2.ht()
    t2.pensize(3)
    blank(get_guessed_word(secret_word,letters_guessed),t2)
    t1=turtle.Turtle()
    t1.color('white')
    t1.ht()
    t1.pensize(3)
    rest(get_available_letters(letters_guessed),t1)
    while guesses >0:
        print('You have %d guess(es) remaining.' % (guesses))
        print('''Unguessed letters: %s\n''' % (get_available_letters(letters_guessed)))
        t1.clear()
        t1=turtle.Turtle()
        t1.color('white')
        t1.ht()
        t1.pensize(3)
        rest(get_available_letters(letters_guessed),t1)
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
                show_possible_matches(g, letters_guessed)
                guesses -= 1
                t3.clear()
                t3=turtle.Turtle()
                t3.ht()
                t3.color('white')
                t3.pensize(3)
                rem(guesses,t3)
                if guesses == 5:
                    head(t)   
                elif guesses == 4:
                    body(t)
                elif guesses == 3:
                    larm(t)
                elif guesses == 2:
                    rarm(t)
                elif guesses == 1:
                    lleg(t)
                elif guesses == 0:
                    print("You've failed. The answer is %s" % (secret_word))
                    rleg(t)
                    dead(secret_word, t)
                    i=input('Press any key to continue.')
                    t1.clear()
                    t2.clear()
                    t3.clear()
                    t.clear()
                    t7=turtle.Turtle()
                    t7.ht()
                    t7.fillcolor('black')
                    t7.setposition(-300,215)
                    t7.begin_fill()
                    t7.setposition(196, 215)
                    t7.setposition(-350,215)
                    t7.setposition(-350,270)
                    t7.setposition(100,270)
                    t7.setposition(100,280)
                    t7.setposition(350,280)
                    t7.setposition(350,224)
                    t7.setposition(196,224)
                    t7.setposition(196,215)
                    t7.end_fill()
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
            t2.clear()
            t2=turtle.Turtle()
            t2.color('white')
            t2.ht()
            t2.pensize(3)
            blank(get_guessed_word(secret_word,letters_guessed),t2)
            victory(secret_word, t)
            i=input('Press any key to continue.')
            t7=turtle.Turtle()
            t7.ht()
            t7.fillcolor('black')
            t7.setposition(-300,215)
            t7.begin_fill()
            t7.setposition(196, 215)
            t7.setposition(-350,215)
            t7.setposition(-350,270)
            t7.setposition(100,270)
            t7.setposition(100,280)
            t7.setposition(350,280)
            t7.setposition(350,224)
            t7.setposition(196,224)
            t7.setposition(196,215)
            t7.end_fill()
            t1.clear()
            t2.clear()
            t3.clear()
            t.clear()
            break
        else:
            if inp not in secret_word:
                print("""Sorry, '%s' is not in the word.\n""" % (inp))
                guesses -= 1
                t3.clear()
                t3=turtle.Turtle()
                t3.ht()
                t3.color('white')
                t3.pensize(3)
                rem(guesses,t3)
                if guesses == 5:
                    head(t)
                elif guesses == 4:
                    body(t)
                elif guesses == 3:
                    larm(t)
                elif guesses == 2:
                    rarm(t)
                elif guesses == 1:
                    lleg(t)
                elif guesses == 0:
                    print("You've failed. The answer is %s" % (secret_word))
                    rleg(t)
                    dead(secret_word, t)
                    i=input('Press any key to continue.')
                    t1.clear()
                    t2.clear()
                    t3.clear()
                    t.clear()
                    t7=turtle.Turtle()
                    t7.ht()
                    t7.fillcolor('black')
                    t7.setposition(-300,215)
                    t7.begin_fill()
                    t7.setposition(196, 215)
                    t7.setposition(-350,215)
                    t7.setposition(-350,270)
                    t7.setposition(100,270)
                    t7.setposition(100,280)
                    t7.setposition(350,280)
                    t7.setposition(350,224)
                    t7.setposition(196,224)
                    t7.setposition(196,215)
                    t7.end_fill()
                    break
            else:
                print("""Good job, '%s is in the word.\n""" % (inp))
            print('''So far you got: %s\n\n\n''' % (get_guessed_word(secret_word,letters_guessed)))
            t2.clear()
            t2=turtle.Turtle()
            t2.color('white')
            t2.ht()
            t2.pensize(3)
            blank(get_guessed_word(secret_word,letters_guessed),t2)
s = turtle.Screen()
turtle.setup(700,700)
turtle.tracer(0,0)
while True:    
    secret_word = choose_word(wordlist)
    s.bgcolor('black')
    t=turtle.Turtle()
    t.color('white')
    t.pensize(3)
    t.ht()
    t.penup()
    t.setposition(-300,270)
    t.pendown()
    t.write('Hangman Game',  align='left', font=('Arial', 40, 'bold') )
    t4=turtle.Turtle()
    t4.penup()
    t4.color('white')
    t4.pensize(3)
    t4.ht()
    t4.setposition(-60,0)
    t4.write('Write 1 in the command to play with hints\nand 2 to play without hints',  align='center', font=('Arial', 20, 'bold') )
    t.penup()#hanger
    t.setposition(200,200) 
    t.pendown()
    t.setposition(200,220)
    t.setposition(300,220)
    t.setposition(300,-300)
    t.setposition(350,-300)
    t.setposition(-350,-300)#hanger done
    turtle.update()
    inp1 = input('Write 1 to play with hint and 2 to play without: ')
    if inp1 == '2':
        t4.clear()
        t4 = turtle.Turtle()
        t4.ht()
        del t4
        t6=turtle.Turtle()
        t6.fillcolor('black')
        t6.ht()
        t6.setposition(0,-10)
        t6.begin_fill()
        t6.setposition(250,-10)
        t6.setposition(250,100)
        t6.setposition(-350,100)
        t6.setposition(-350,-10)
        t6.setposition(250,-10)
        t6.end_fill()
        t7=turtle.Turtle()
        t7.ht()
        t7.fillcolor('black')
        t7.setposition(-300,215)
        t7.begin_fill()
        t7.setposition(196, 215)
        t7.setposition(-350,215)
        t7.setposition(-350,270)
        t7.setposition(100,270)
        t7.setposition(100,280)
        t7.setposition(350,280)
        t7.setposition(350,224)
        t7.setposition(196,224)
        t7.setposition(196,215)
        t7.end_fill()
        turtle.update()
        hangman(secret_word)
        turtle.update()
    elif inp1 == '1':
        t4.clear()
        t4=turtle.Turtle()
        t4.ht()
        del t4
        t6=turtle.Turtle()
        t6.fillcolor('black')
        t6.ht()
        t6.setposition(0,-10)
        t6.begin_fill()
        t6.setposition(250,-10)
        t6.setposition(250,100)
        t6.setposition(-350,100)
        t6.setposition(-350,-10)
        t6.setposition(250,-10)
        t6.end_fill()
        t7=turtle.Turtle()
        t7.ht()
        t7.fillcolor('black')
        t7.setposition(-300,215)
        t7.begin_fill()
        t7.setposition(196, 215)
        t7.setposition(-350,215)
        t7.setposition(-350,270)
        t7.setposition(100,270)
        t7.setposition(100,280)
        t7.setposition(350,280)
        t7.setposition(350,224)
        t7.setposition(196,224)
        t7.setposition(196,215)
        t7.end_fill()
        turtle.update()
        t5=turtle.Turtle()
        t5.penup()
        t5.color('yellow')
        t5.pensize(3)
        t5.ht()
        t5.setposition(-300,220)
        t5.write("Write ' * ' in the command to use hint\nPossible words will be shown in the commmand.", align='left', font=('Arial', 15, 'bold'))
        turtle.update()
        hangman_with_hints(secret_word)
        turtle.update()
    else:
        print('Write 1 or  2.')
turtle.done()
