# IPND Stage 2 Final Project

#initial easy paragraph (fill in __1__)
easy_paragraph = '\nYou\'ve chosen EASY!\n\nYou will get five guesses per problem\n\nYou can run python in your text editor OR your __1__. We use an ___2___ statement to assign variables to strings! A string is just a sequence of ___3___ surrounded by quotes. We often use variables and strings inside of procedures. Another name for a procedure is a ___4___.'
#second easy paragraph (fill in __2__)
easy_paragraph2 = '\nYou can run python in your text editor OR your command line. We use an ___2___ statement to assign variables to strings! A string is just a sequence of ___3___ surrounded by quotes. We often use variables and strings inside of procedures. Another name for a procedure is a ___4___.'
#third easy paragraph (fill in __3__)
easy_paragraph3 = '\nYou can run python in your text editor OR your command line. We use an assignment statement to assign variables to strings! A string is just a sequence of ___3___ surrounded by quotes. We often use variables and strings inside of procedures. Another name for a procedure is a ___4___.'
#fourth easy paragraph (fill in __4__)
easy_paragraph4 = '\nYou can run python in your text editor OR your command line. We use an assignment statement to assign variables to strings! A string is just a sequence of characters surrounded by quotes. We often use variables and strings inside of procedures. Another name for a procedure is a ___4___.'
#final solution with quiz answers filled in
final_solution = '\nYou can run python in your text editor OR your command line. We use an assignment statement to assign variables to strings! A string is just a sequence of characters surrounded by quotes. We often use variables and strings inside of procedures. Another name for a procedure is a function.'
#array with answers
easy_answers = ['command line', 'assignment', 'characters', 'function']
#medium quiz (fill in __1__)
medium_paragraph = '\nWe create functions using the ___1___ keyword. If you want to run a block of code as long as a statement is true, you can use a __2__ loop. Conditionals are another great tool at our disposal. Use an __3__ statement to check if something is true. You\'ll want to add an __4__ statement in case it isn\'t true.'
#medium quiz (fill in __2__)
medium_paragraph2 = '\nWe create functions using the def keyword. If you want to run a block of code as long as a statement is true, you can use a __2__ loop. Conditionals are another great tool at our disposal. Use an __3__ statement to check if something is true. You\'ll want to add an __4__ statement in case it isn\'t true.'
#medium quiz (fill in __3__)
medium_paragraph3 = '\nWe create functions using the def keyword. If you want to run a block of code as long as a statement is true, you can use a while loop. Conditionals are another great tool at our disposal. Use an __3__ statement to check if something is true. You\'ll want to add an __4__ statement in case it isn\'t true.'
#fourth medium paragraph (fill in __4__)
medium_paragraph4 = '\nWe create functions using the def keyword. If you want to run a block of code as long as a statement is true, you can use a while loop. Conditionals are another great tool at our disposal. Use an if statement to check if something is true. You\'ll want to add an __4__ statement in case it isn\'t true.'
#medium quiz final solution
medium_final_solution = '\nWe create functions using the def keyword. If you want to run a block of code as long as a statement is true, you can use a while loop. Conditionals are another great tool at our disposal. Use an if statement to check if something is true. You\'ll want to add an else statement in case it isn\'t true.'
#array with medium answers
medium_answers = ['def', 'while', 'if', 'else']

#hard quiz (fill in __1__)
hard_paragraph = '\nStep one of Pythonista\'s guide to solving all problems is to understand the __1__. Step two is to understand the __2__! You can get a users input using the __3__ function. A list inside a list is called a __4__ list'
#hard quiz (fill in __2__)
hard_paragraph2 = '\nStep one of Pythonista\'s guide to solving all problems is to understand the inputs. Step two is to understand the __2__! You can get a users input using the __3__ function. A list inside a list is called a __4__ list'
#hard quiz (fill in __3__)
hard_paragraph3 = '\nStep one of Pythonista\'s guide to solving all problems is to understand the inputs. Step two is to understand the outputs! You can get a users input using the __3__ function. A list inside a list is called a __4__ list'
#hard quiz (fill in __4__)
hard_paragraph4 = '\nStep one of Pythonista\'s guide to solving all problems is to understand the inputs. Step two is to understand the outputs! You can get a users input using the raw_input function. A list inside a list is called a __4__ list'
#hard quiz final solution
hard_final_solution = '\nStep one of Pythonista\'s guide to solving all problems is to understand the inputs. Step two is to understand the outputs! You can get a users input using the raw_input function. A list inside a list is called a nested list'
#array with hard answers
hard_answers = ['inputs', 'outputs', 'raw_input', 'nested']



#initialized guess variable
guess = 5

#function for first easy quiz question
def easy():
    guess = 5
    print easy_paragraph
    one = raw_input('\nWhat should be substituted for __1__?')
    while one != 'command line':
        guess = guess - 1
        if guess == 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guess left! Make it count!'
            one = raw_input('What should be substituted for __1__?')
            print one
        if guess > 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guesses left!'
            one = raw_input('What should be substituted for __1__?')
            print one
        if guess == 0:
            print '\nYou lose!\n'
            on_load()
    if one == 'command line':
        print '\nThat\'s right!'
        return easy2()
#function for second easy quiz question
def easy2():
    guess = 5
    print easy_paragraph2
    two = raw_input('\nWhat should be substituted for __2__?')
    print two
    while two != 'assignment':
        guess = guess - 1
        if guess == 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guess left! Make it count!'
            two = raw_input('\nWhat should be substituted for __2__?')
            print two
        if guess > 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guesses left!'
            two = raw_input('\nWhat should be substituted for __2__?')
            print two
        if guess == 0:
            print '\nYou lose!\n'
            on_load()
    if two == 'assignment':
        print '\nThat\'s right!'
        return easy3()
#function for third easy quiz question
def easy3():
    guess = 5
    print easy_paragraph3
    three = raw_input('\nWhat should be substituted for __3__?')
    print three
    while three != 'characters':
        guess = guess - 1
        if guess == 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guess left! Make it count!'
            three = raw_input('\nWhat should be substituted for __3__?')
            print three
        if guess > 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guesses left!'
            three = raw_input('\nWhat should be substituted for __3__?')
            print three
        if guess == 0:
            print '\nYou lose!\n'
            on_load()
    if three == 'characters':
        print '\nThat\'s right!'
        return easy4()
#function for fourth easy quiz question
def easy4():
    guess = 5
    print easy_paragraph4
    four = raw_input('\nWhat should be substituted for __4__?')
    print four
    while four != 'function':
        guess = guess - 1
        if guess == 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guess left! Make it count!'
            four = raw_input('\nWhat should be substituted for __4__?')
            print four
        if guess > 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guesses left!'
            four = raw_input('\nWhat should be substituted for __4__?')
            print four
        if guess == 0:
            print '\nYou lose!\n'
            on_load()
    if four == 'function':
        print '\nYay! You win! The final solution is:'
        print final_solution
        print '\n'
        on_load()

#function for first medium quiz question
def medium():
    guess = 5
    print medium_paragraph
    one = raw_input('\nWhat should be substituted for __1__?')
    while one != 'def':
        guess = guess - 1
        if guess == 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guess left! Make it count!'
            one = raw_input('What should be substituted for __1__?')
            print one
        if guess > 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guesses left!'
            one = raw_input('What should be substituted for __1__?')
            print one
        if guess == 0:
            print '\nYou lose!\n'
            on_load()
    if one == 'def':
        print '\nThat\'s right!'
        return medium2()
#function for second medium quiz question
def medium2():
    guess = 5
    print medium_paragraph2
    two = raw_input('\nWhat should be substituted for __2__?')
    print two
    while two != 'while':
        guess = guess - 1
        if guess == 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guess left! Make it count!'
            two = raw_input('\nWhat should be substituted for __2__?')
            print two
        if guess > 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guesses left!'
            two = raw_input('\nWhat should be substituted for __2__?')
            print two
        if guess == 0:
            print '\nYou lose!\n'
            on_load()
    if two == 'while':
        print '\nThat\'s right!'
        return medium3()
#function for third medium quiz question
def medium3():
    guess = 5
    print medium_paragraph3
    three = raw_input('\nWhat should be substituted for __3__?')
    print three
    while three != 'if':
        guess = guess - 1
        if guess == 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guess left! Make it count!'
            three = raw_input('\nWhat should be substituted for __3__?')
            print three
        if guess > 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guesses left!'
            three = raw_input('\nWhat should be substituted for __3__?')
            print three
        if guess == 0:
            print '\nYou lose!\n'
            on_load()
    if three == 'if':
        print '\nThat\'s right!'
        return medium4()
#function for fourth medium quiz question
def medium4():
    guess = 5
    print medium_paragraph4
    four = raw_input('\nWhat should be substituted for __4__?')
    print four
    while four != 'else':
        guess = guess - 1
        if guess == 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guess left! Make it count!'
            four = raw_input('\nWhat should be substituted for __4__?')
            print four
        if guess > 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guesses left!'
            four = raw_input('\nWhat should be substituted for __4__?')
            print four
        if guess == 0:
            print '\nYou lose!\n'
            on_load()
    if four == 'else':
        print '\nYay! You win! The final solution is:'
        print medium_final_solution
        print '\n'
        on_load()

#function for first hard quiz question
def hard():
    guess = 5
    print hard_paragraph
    one = raw_input('\nWhat should be substituted for __1__?')
    while one != 'inputs':
        guess = guess - 1
        if guess == 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guess left! Make it count!'
            one = raw_input('What should be substituted for __1__?')
            print one
        if guess > 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guesses left!'
            one = raw_input('What should be substituted for __1__?')
            print one
        if guess == 0:
            print '\nYou lose!\n'
            on_load()
    if one == 'inputs':
        print '\nThat\'s right!'
        return hard2()
#function for second hard medium quiz question
def hard2():
    guess = 5
    print hard_paragraph2
    two = raw_input('\nWhat should be substituted for __2__?')
    print two
    while two != 'outputs':
        guess = guess - 1
        if guess == 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guess left! Make it count!'
            two = raw_input('\nWhat should be substituted for __2__?')
            print two
        if guess > 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guesses left!'
            two = raw_input('\nWhat should be substituted for __2__?')
            print two
        if guess == 0:
            print '\nYou lose!\n'
            on_load()
    if two == 'outputs':
        print '\nThat\'s right!'
        return hard3()
#function for third hard quiz question
def hard3():
    guess = 5
    print hard_paragraph3
    three = raw_input('\nWhat should be substituted for __3__?')
    print three
    while three != 'raw_input':
        guess = guess - 1
        if guess == 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guess left! Make it count!'
            three = raw_input('\nWhat should be substituted for __3__?')
            print three
        if guess > 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guesses left!'
            three = raw_input('\nWhat should be substituted for __3__?')
            print three
        if guess == 0:
            print '\nYou lose!\n'
            on_load()
    if three == 'raw_input':
        print '\nThat\'s right!'
        return hard4()
#function for fourth hard quiz question
def hard4():
    guess = 5
    print hard_paragraph4
    four = raw_input('\nWhat should be substituted for __4__?')
    print four
    while four != 'nested':
        guess = guess - 1
        if guess == 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guess left! Make it count!'
            four = raw_input('\nWhat should be substituted for __4__?')
            print four
        if guess > 1:
            print '\nThat isn\'t the correct answer. You have ' + str(guess) + ' guesses left!'
            four = raw_input('\nWhat should be substituted for __4__?')
            print four
        if guess == 0:
            print '\nYou lose!\n'
            on_load()
    if four == 'nested':
        print '\nYay! You win! The final solution is:'
        print hard_final_solution
        print '\n'
        on_load()
#Start game/on load/ pick difficulty level function
def on_load():
    select_level_input = raw_input('Please select a game difficulty level by typing it in! \nPossible choices include easy, medium, and hard. ')
    print select_level_input
    if select_level_input == 'easy':
        return easy()
    if select_level_input == 'medium':
        return medium()
    if select_level_input == 'hard':
        return hard()
    else:
        on_load()
on_load()

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.\n
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,w
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

#sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
#adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
#don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
#tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?
