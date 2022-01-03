"""The module contains the rules of the game and its functions."""
from random import randint


def printing_rule():
    """Print game rules."""
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")


def correct_answer():
    """
    Generate question number and return correct answer.

    Returns:
            cor_answer.
    """
    lower_bound = 0
    upper_bound = 1500
    num = randint(lower_bound, upper_bound)  # noqa: S311
    print('Question: {0}'.format(num))
    cor_answer = 'yes' if num % 2 == 0 else 'no'
    return cor_answer  # noqa: WPS331


def user_answer():
    """
    Asks the user for his answer and return his.

    Returns:
            u_answer.
    """
    u_answer = input('Your answer: ')
    return u_answer  # noqa: WPS331
