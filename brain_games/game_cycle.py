"""The module contains the basic logic of game execution."""
import prompt


def game_cycle(game_logic):
    """
    Run main cycle of game.

    Parameters:
        game_logic: module of the game
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    if user_name:
        print('Hello, {0}!'.format(user_name))
        print(game_logic.GAME_RULE)
    flag = 0
    while flag < 3:
        correct_answer, question_string = game_logic.correct_answer()
        print('Question: {0}'.format(question_string))
        user_answer = input('Your answer: ')
        if correct_answer == user_answer:
            print('Correct!')
            flag += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
                user_answer, correct_answer,
            ))
            print("Let's try again, {0}!".format(user_name))
            break

    if flag == 3:
        print('Congratulations, {0}!'.format(user_name))
