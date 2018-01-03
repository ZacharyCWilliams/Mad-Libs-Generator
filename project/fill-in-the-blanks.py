# IPND Stage 2 Final Project
#dictionary containing all game data: level, quiz, answer, and number of guesses
game_data = {
    'easy': {
    'quiz': '\nYou can run python in your text editor OR your __1__. We use an __2__ statement to assign variables to strings! A string is just a sequence of __3__ surrounded by quotes. We often use variables and strings inside of procedures. Another name for a procedure is a __4__.',
    'answers': ['command line', 'assignment', 'characters', 'function'],
    'number_of_guesses': 5,
    'start_index': 1
    },
    'medium': {
    'quiz': '\nWe create functions using the __1__ keyword. If you want to run a block of code as long as a statement is true, you can use a __2__ loop. Conditionals are another great tool at our disposal. Use an __3__ statement to check if something is true. You\'ll want to add an __4__ statement in case it isn\'t true.',
    'answers': ['def', 'while', 'if', 'else'],
    'number_of_guesses': 5,
    'start_index': 1
    },
    'hard': {
    'quiz': '\nStep one of Pythonista\'s guide to solving all problems is to understand the __1__. Step two is to understand the __2__! You can get a users input using the __3__ function. A list inside a list is called a __4__ list',
    'answers': ['inputs', 'outputs', 'raw_input', 'nested'],
    'number_of_guesses': 5,
    'start_index': 1
    }
}

one_guess = 1
two_guesses_left = 2
increment_index_by_one = 1
decrement_index_by_one = 1
last_index_of_playable_game = 4
game_over_index = 5
refill_guesses = 5

def incorrect_guess(user_input, answer, quiz, answers, index, start_index, number_of_guesses):
    if (user_input != answer):
        if (number_of_guesses > two_guesses_left):
            number_of_guesses = number_of_guesses - one_guess
            print '\nOops! That\'s not right. You have ' + str(number_of_guesses) + ' guesses left! Try again:'
            check_input(quiz, answers, start_index, number_of_guesses, index, answer)
        elif (number_of_guesses == two_guesses_left):
            number_of_guesses = number_of_guesses - one_guess
            print '\nOops! That\'s not right. This is your LAST guess: make it count!'
            check_input(quiz, answers, start_index, number_of_guesses, index, answer)
        elif (number_of_guesses == one_guess):
                print '\nYou Lose! Let\'s play again!\n'
                pick_a_level()

def you_won(index, answer, quiz):
    quiz = quiz.replace('__' + str(index) + '__', answer)
    print '\nYay! You won! The final solution is:'
    print quiz + '\n'
    pick_a_level()

def correct_answers(user_input, answer, quiz, answers, index, start_index, number_of_guesses):
    print '\nThat\'s right!'
    quiz = quiz.replace('__' + str(index) + '__', answer)
    print quiz
    index = index + increment_index_by_one
    if (index < last_index_of_playable_game):
        answer = answers[index - increment_index_by_one]
        check_input(quiz, answers, start_index, number_of_guesses, index, answer)
    if (index == last_index_of_playable_game):
        answer = answers[index - decrement_index_by_one]
        check_input(quiz, answers, start_index, number_of_guesses, index, answer)
    if (index == game_over_index):
        you_won(index, answer, quiz)
        return



def check_input(quiz, answers, start_index, number_of_guesses, index, answer):
       while True:
            user_input = raw_input('\nWhat should be substituted for __' + str(index) + '__? ')
            if (user_input == answer):
                number_of_guesses = refill_guesses
                correct_answers(user_input, answer, quiz, answers, index, start_index, number_of_guesses)
            elif (user_input != answer):
                incorrect_guess(user_input, answer, quiz, answers, index, start_index, number_of_guesses)

def setup_variables(select_level):
    quiz = game_data[select_level]['quiz']
    answers = game_data[select_level]['answers']
    start_index = game_data[select_level]['start_index']
    number_of_guesses = game_data[select_level]['number_of_guesses']
    for index, answer in enumerate(answers, start_index):
        return check_input(quiz, answers, start_index, number_of_guesses, index, answer)



def print_paragraph(select_level):
        print '\nYou\'ve chosen ' + str(select_level) + '! You will get five guesses per problem'
        #print quiz paragraph from level chosen
        paragraph = game_data[select_level]['quiz']
        print paragraph
        #move onto game play!
        return setup_variables(select_level)

#Game loads with this function
def pick_a_level():
    #user selects game level by typing in easy, medium, or hard
    select_level = raw_input('Please select a game difficulty level by typing it in! \nPossible choices include easy, medium, and hard. ')
    #if user input != viable game level ask again
    if select_level != 'easy' and select_level != 'medium' and select_level != 'hard':
        print '\nOops! That didn\'t work. Try again:\n'
        pick_a_level()
    else:
        print_paragraph(select_level)
pick_a_level()
