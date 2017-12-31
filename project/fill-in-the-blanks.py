blanks_to_fill_in = ['__1__', '__2__', '__3__', '__4__']

game_data = {
    'easy': {
    'quiz': '\nYou can run python in your text editor OR your __1__. We use an ' + blanks_to_fill_in[1] + ' statement to assign variables to strings! A string is just a sequence of ' + blanks_to_fill_in[2] + ' surrounded by quotes. We often use variables and strings inside of procedures. Another name for a procedure is a' + blanks_to_fill_in[3] + '.',
    'answers': ['command line', 'assignment', 'characters', 'function'],
    'number_of_guesses': 5
    },
    'medium': {
    'quiz': '\nWe create functions using the ___1___ keyword. If you want to run a block of code as long as a statement is true, you can use a __2__ loop. Conditionals are another great tool at our disposal. Use an __3__ statement to check if something is true. You\'ll want to add an __4__ statement in case it isn\'t true.',
    'answers': ['def', 'while', 'if', 'else'],
    'number_of_guesses': 5
    },
    'hard': {
    'quiz': '\nStep one of Pythonista\'s guide to solving all problems is to understand the __1__. Step two is to understand the __2__! You can get a users input using the __3__ function. A list inside a list is called a __4__ list',
    'answers': ['inputs', 'outputs', 'raw_input', 'nested'],
    'number_of_guesses': 5
    }
}


def game_play():
    number_of_guesses = game_data[select_level]['number_of_guesses']
    first_question = raw_input('\nWhat should be substituted for __1__? ')
    if first_question == game_data[select_level]['answers'][0]:
        replace_quiz = game_data[select_level]['quiz']
        replace_answer = game_data[select_level]['answers'][0]
        replace_quiz.replace('__1__', replace_answer)
        print '\nThat\'s right!'
        print game_data[select_level]['quiz']



    if first_question != game_data[select_level]['answers'][0]:
        number_of_guesses = game_data[select_level]['number_of_guesses'] - 1

        print number_of_guesses
        second_question = raw_input('\nWhat should be substituted for __2__? ')
        if second_question == game_data[select_level]['answers'][1]:
            print 'this is working'
            third_question = raw_input('\nWhat should be substituted for __3__? ')
            if third_question == game_data[select_level]['answers'][2]:
                print 'this is working'
                fourth_question = raw_input('\nWhat should be substituted for __4__? ')
                if fourth_question == game_data[select_level]['answers'][3]:
                    print 'this is working'
#user selects game difficulty
select_level = None
#Game loads with this function
def on_load():
    global select_level
    select_level = raw_input('Please select a game difficulty level by typing it in! \nPossible choices include easy, medium, and hard. ')
    #if user input != viable game level ask again
    if select_level != 'easy' and select_level != 'medium' and select_level != 'hard':
        print '\nOops! That didn\'t work. Try again:\n'
        on_load()
    else:
        print '\nYou\'ve chosen ' + str(select_level) + '! You will get five guesses per problem'
        #print quiz paragraph from level chosen
        paragraph = game_data[select_level]['quiz']
        print paragraph
        #move onto game play!
        return game_play()
on_load()
