# IPND Stage 2 Final Project
"""
    game_data = data structure containing all game data: level, quiz, answer, start_index and number of guesses
"""

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
"""
Variables
"""
one_guess = 1
two_guesses_left = 2
increment_index_by_one = 1
decrement_index_by_one = 1
last_index_of_playable_game = 4
game_over_index = 5
refill_guesses = 5

"""incorrect_guess()

  Args:
      param1: quiz
      param2: answers
      param3: start_index
      param4: number_of_guesses
      param5: index
      param6: answer
      param7: user_input
  Behavior:
      1. Checks to see how many guesses are left
      2. Reduces number of guesses left by one
      3. Sends new info back to check_input
      4. If number of guesses left = 0, prints 'you lose' and restarts game

  Returns:
      1. quiz
      2. answers
      3. start_index
      4. number_of_guesses
      5. index
      6. answer
  """

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

"""you_won()

  Args:
      param1: quiz
      param2: index
      param3: answer
  Behavior:
      1. Prints final solution
      2. restart game!

  """

def you_won(index, answer, quiz):
    quiz = quiz.replace('__' + str(index) + '__', answer)
    print '\nYay! You won! The final solution is:'
    print quiz + '\n'
    pick_a_level()

"""correct_answers()

  Args:
      param1: quiz
      param2: answers
      param3: start_index
      param4: number_of_guesses
      param5: index
      param6: answer
      param7: user_input
  Behavior:
      1. Prints: That's right!
      2. Creates and prints new version of quiz (with correctly inputed answer filled in)
      3. Checks if all questions have been answered, if so moves to you_won function

  Returns:
      1. answer
      2. user_input
  """

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

"""check_input()

  Args:
      param1: quiz
      param2: answers
      param3: start_index
      param4: number_of_guesses
      param5: index
      param6: answer
  Behavior:
      1. Gets user input
      2. Checks if user input == answer. If so, pass all data onto correct_answers
      3. If input != answer, pass all data onto incorrect_guess
  Returns:
      1. answer
      2. user_input
  """


def check_input(quiz, answers, start_index, number_of_guesses, index, answer):
       while True:
            user_input = raw_input('\nWhat should be substituted for __' + str(index) + '__? ')
            if (user_input == answer):
                number_of_guesses = refill_guesses
                correct_answers(user_input, answer, quiz, answers, index, start_index, number_of_guesses)
            elif (user_input != answer):
                incorrect_guess(user_input, answer, quiz, answers, index, start_index, number_of_guesses)

"""setup_variables()

  Args:
      param1: select_level (user selected level)
  Behavior:
      1. Sets all variables dependent on game_data structure
      2. Passes these variables as parameters into check_input()
  Returns:
      1. quiz
      2. answers
      3. start_index
      4. number_of_guesses
      5. index
      6. answer
  """

def setup_variables(select_level):
    quiz = game_data[select_level]['quiz']
    answers = game_data[select_level]['answers']
    start_index = game_data[select_level]['start_index']
    number_of_guesses = game_data[select_level]['number_of_guesses']
    for index, answer in enumerate(answers, start_index):
        return check_input(quiz, answers, start_index, number_of_guesses, index, answer)


"""Pick_a_level()

  Args:
      param1: select_level (user selected level)
  Behavior:
      1. Print statement with chosen level
      2. Pull/Print selected level's quiz
      3. Pass selected level onto setup_variables()
  Returns:
      setup_variables(select_level)
  """


def print_paragraph(select_level):
        print '\nYou\'ve chosen ' + str(select_level) + '! You will get five guesses per problem'
        #print quiz paragraph from level chosen
        paragraph = game_data[select_level]['quiz']
        print paragraph
        #move onto game play!
        return setup_variables(select_level)

"""Pick_a_level()

  Behavior:
      1. Asks user to select a difficulty level by typing in easy, medium, or hard
      2. If user inputs something other than a viable level, user is asked for input again
      3. Once user selects a level, we pass that level onto print_paragraph()
      4. Note: This function starts once the game loads
  Returns:
      Returns select_level (User selected level)
  """
def pick_a_level():
    select_level = raw_input('Please select a game difficulty level by typing it in! \nPossible choices include easy, medium, and hard. ')
    if select_level != 'easy' and select_level != 'medium' and select_level != 'hard':
        print '\nOops! That didn\'t work. Try again:\n'
        pick_a_level()
    else:
        print_paragraph(select_level)
pick_a_level()
