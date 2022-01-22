"""The module contains the rules of the game and its functions."""
from random import randint

RULE = "Answer 'yes' if the number is even, otherwise answer 'no'."


def check_even(number):
    """
    Check whether a number is even.

    Parameters:
        number: int

    Returns:
            True.
    """
    if number % 2 == 0:
        return True


def correct_answer():
    """
    Generate question number and return correct answer.

    Returns:
            cor_answer,
            question_string.
    """
    bound = (0, 1500)
    num = randint(bound[0], bound[1])
    cor_answer = 'yes' if check_even(num) else 'no'
    return cor_answer, num
