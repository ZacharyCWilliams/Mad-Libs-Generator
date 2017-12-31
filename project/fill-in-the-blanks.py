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


def game_play():
    #pulling number of guesses allowed from game_data structure
    number_of_guesses = game_data[select_level]['number_of_guesses']
    #asking user for their first answer
    first_question = raw_input('\nWhat should be substituted for __1__? ')
    #pulling correct answer from data structure
    first_answer = game_data[select_level]['answers'][0]
    #as long as they guess incorrectly, let them know they're wrong, reduce number of guesses by 1, and ask again
    while first_question != first_answer:
        if number_of_guesses > 2:
            number_of_guesses = number_of_guesses - 1
            print '\nOops! That\'s not right. You have ' + str(number_of_guesses) + ' guesses left! Try again:'
            first_question = raw_input('\nWhat should be substituted for __1__? ')
        elif number_of_guesses == 2:
            number_of_guesses = number_of_guesses - 1
            print '\nOops! That\'s not right. This is your LAST guess: make it count!'
            first_question = raw_input('\nWhat should be substituted for __1__? ')
        else:
            #if number_of_guesses == 0 reset game
            print '\nYou Lose! Let\'s play again!'
            on_load()


    #if they're correct print the new version of the quiz with first answer filled in!
    if first_question == first_answer:
        replace_quiz = game_data[select_level]['quiz']
        replace_quiz = replace_quiz.replace('__1__', first_answer)
        print '\nThat\'s right!'
        print replace_quiz

        #moving on to Question 2
        second_question = raw_input('\nWhat should be substituted for __2__? ')
        #setting second answer (pulling from data set)
        second_answer = game_data[select_level]['answers'][1]
        #resetting number of guesses
        number_of_guesses = 5

        while second_question != second_answer:
            if number_of_guesses > 2:
                #as long as they guess incorrectly, let them know they're wrong, reduce number of guesses by 1, and ask again
                number_of_guesses = number_of_guesses - 1
                print '\nOops! That\'s not right. You have ' + str(number_of_guesses) + ' guesses left! Try again:'
                second_question = raw_input('\nWhat should be substituted for __2__? ')
            elif number_of_guesses == 2:
                number_of_guesses = number_of_guesses - 1
                print '\nOops! That\'s not right. This is your LAST guess: make it count!'
                second_question = raw_input('\nWhat should be substituted for __2__? ')
            else:
                print '\nYou Lose! Let\'s play again!'
                on_load()

        if second_question == second_answer:
            replace_quiz = replace_quiz.replace('__2__', second_answer)
            print '\nThat\'s right!'
            print replace_quiz

            third_question = raw_input('\nWhat should be substituted for __3__? ')
            third_answer = game_data[select_level]['answers'][2]
            number_of_guesses = 5

            while third_question != third_answer:
                if number_of_guesses > 2:
                    #as long as they guess incorrectly, let them know they're wrong, reduce number of guesses by 1, and ask again
                    number_of_guesses = number_of_guesses - 1
                    print '\nOops! That\'s not right. You have ' + str(number_of_guesses) + ' guesses left! Try again:'
                    third_question = raw_input('\nWhat should be substituted for __3__? ')
                elif number_of_guesses == 2:
                    number_of_guesses = number_of_guesses - 1
                    print '\nOops! That\'s not right. This is your LAST guess: make it count!'
                    third_question = raw_input('\nWhat should be substituted for __3__? ')
                else:
                    print '\nYou Lose! Let\'s play again!'
                    on_load()



            if third_question == third_answer:
                replace_quiz = replace_quiz.replace('__3__', third_answer)
                print '\nThat\'s right!'
                print replace_quiz

                fourth_question = raw_input('\nWhat should be substituted for __4__? ')
                fourth_answer = game_data[select_level]['answers'][3]
                number_of_guesses = 5

                while fourth_question != fourth_answer:
                    if number_of_guesses > 2:
                        #as long as they guess incorrectly, let them know they're wrong, reduce number of guesses by 1, and ask again
                        number_of_guesses = number_of_guesses - 1
                        print '\nOops! That\'s not right. You have ' + str(number_of_guesses) + ' guesses left! Try again:'
                        fourth_question = raw_input('\nWhat should be substituted for __4__? ')
                    elif number_of_guesses == 2:
                        number_of_guesses = number_of_guesses - 1
                        print '\nOops! That\'s not right. This is your LAST guess: make it count!'
                        fourth_question = raw_input('\nWhat should be substituted for __4__? ')
                    else:
                        print '\nYou Lose! Let\'s play again!'
                        on_load()

                if fourth_question == fourth_answer:
                    #if they're correct print the new version of the quiz with first answer filled in!
                    replace_quiz = replace_quiz.replace('__4__', fourth_answer)
                    print '\nYay! You Win! The final version is:'
                    #print finalized version of quiz
                    print replace_quiz
                    print '\n'
                    #when user wins restart game!
                    on_load()

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
