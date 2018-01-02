# IPND Stage 2 Final Project
#dictionary containing all game data: level, quiz, answer, and number of guesses
game_data = {
    'easy': {
    'quiz': '\nYou can run python in your text editor OR your __1__. We use an __2__ statement to assign variables to strings! A string is just a sequence of __3__ surrounded by quotes. We often use variables and strings inside of procedures. Another name for a procedure is a __4__.',
    'answers': ['command line', 'assignment', 'characters', 'function'],
    'number_of_guesses': 5
    },
    'medium': {
    'quiz': '\nWe create functions using the __1__ keyword. If you want to run a block of code as long as a statement is true, you can use a __2__ loop. Conditionals are another great tool at our disposal. Use an __3__ statement to check if something is true. You\'ll want to add an __4__ statement in case it isn\'t true.',
    'answers': ['def', 'while', 'if', 'else'],
    'number_of_guesses': 5
    },
    'hard': {
    'quiz': '\nStep one of Pythonista\'s guide to solving all problems is to understand the __1__. Step two is to understand the __2__! You can get a users input using the __3__ function. A list inside a list is called a __4__ list',
    'answers': ['inputs', 'outputs', 'raw_input', 'nested'],
    'number_of_guesses': 5
    }
}

quiz = None
answers = None
start_index = None
number_of_guesses = None
user_input = None
answer = None
index = None

#global variables aren't working properly

def incorrect_guess():
    print answers
    global number_of_guesses
    print number_of_guesses
    print quiz
    global user_input
    global answer

    if (user_input == answer):
        return
    while (user_input != answer):
        if (number_of_guesses > 2):
            number_of_guesses = number_of_guesses - 1
            print '\nOops! That\'s not right. You have ' + str(number_of_guesses) + ' guesses left! Try again:'
            user_input = raw_input('What should be substituted for __' + str(index) + '__?')
        elif (number_of_guesses == 2):
            number_of_guesses = number_of_guesses - 1
            print '\nOops! That\'s not right. This is your LAST guess: make it count!'
            user_input = raw_input('What should be substituted for __' + str(index) + '__?')
        elif (number_of_guesses == 1):
                print '\nYou Lose! Let\'s play again!\n'
                on_load()


def game_play():
    global quiz
    quiz = game_data[select_level]['quiz']
    global answers
    answers = game_data[select_level]['answers']
    global start_index
    start_index = 1
    global number_of_guesses
    number_of_guesses = game_data[select_level]['number_of_guesses']
    global answer
    global index

    for index, answer in enumerate(answers, start_index):
        while True:
            global user_input
            user_input = raw_input('\nWhat should be substituted for __' + str(index) + '__? ')
            if (user_input == answer):
                print '\nThat\'s right!'
                quiz = quiz.replace('__' + str(index) + '__', answer)
                print quiz
                index = index + 1
                if index <= 4:
                    answer = answers[index- 1]
                if index == 5:
                    quiz = quiz.replace('__' + str(index) + '__', answer)
                    print '\nYay! You won! The final solution is:'
                    print quiz + '\n'
                    on_load()
            elif (user_input != answer):
                incorrect_guess()


#set global variable to None so that all functions can access variable && we can set/reset variable in local scopes
select_level = None
#Game loads with this function
def on_load():
    global select_level
    #user selects game level by typing in easy, medium, or hard
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
