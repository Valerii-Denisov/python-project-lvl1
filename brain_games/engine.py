"""The module contains the basic logic of game execution."""
import prompt


def start_game(game):
    """
    Run main cycle of game.

    Parameters:
        game: module of the game
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    if user_name:
        print('Hello, {0}!'.format(user_name))
        print(game.RULE)
    for _ in range(3):
        correct_answer, question_string = game.get_game_data()
        print('Question: {0}'.format(question_string))
        user_answer = input('Your answer: ')
        if correct_answer == user_answer:
            print('Correct!')
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
                user_answer, correct_answer,
            ))
            print("Let's try again, {0}!".format(user_name))
            return
    print('Congratulations, {0}!'.format(user_name))
