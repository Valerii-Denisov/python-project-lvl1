"""The module contains the rules of the game and its functions."""
from random import randint

RULE = "Answer 'yes' if the number is even, otherwise answer 'no'."
BOUND = (0, 1500)


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


def get_correct_answer():
    """
    Generate question number and return correct answer.

    Returns:
            cor_answer,
            question_string.
    """
    num = randint(BOUND[0], BOUND[1])
    cor_answer = 'yes' if check_even(num) else 'no'
    return cor_answer, num
