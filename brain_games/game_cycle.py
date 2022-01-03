"""The module contains the basic logic of game execution."""
import prompt


def greet():
    """
    Display a greeting.

    Returns:
            user_name.
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    if user_name:
        print('Hello, {0}!'.format(user_name))
    return user_name


def game_cycle(game_logic, user_name):
    """
    Run main cycle of game.

    Parameters:
        game_logic: module of the game
        user_name: str
    """
    flag = 0
    while flag < 3:
        correct_answer = game_logic.correct_answer()
        user_answer = game_logic.user_answer()
        if correct_answer == user_answer:
            print('Correct!')
            flag += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
                user_answer, correct_answer,
            ))
            print("Let's try again, {0}.".format(user_name))
            break

    if flag == 3:
        print('Congratulations, {0}!'.format(user_name))
