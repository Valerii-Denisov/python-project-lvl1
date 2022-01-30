"""The module contains the rules of the game and its functions."""
from random import randint

RULES = "Answer 'yes' if the number is even, otherwise answer 'no'."
BOUNDS = (0, 1500)


def is_even(number):
    """
    Check whether a number is even.

    Parameters:
        number: int

    Returns:
            True or False.
    """
    return number % 2 == 0


def get_game_data():
    """
    Generate question number and return correct answer.

    Returns:
            cor_answer,
            question_string.
    """
    num = randint(*BOUNDS)
    cor_answer = 'yes' if is_even(num) else 'no'
    return cor_answer, num
