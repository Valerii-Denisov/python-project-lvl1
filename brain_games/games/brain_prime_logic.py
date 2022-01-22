"""The module contains the rules of the game and its functions."""
from random import randint

RULE = "Answer 'yes' if the number is prime, otherwise answer 'no'."


def check_prime(number):
    """
    Check whether a number is prime.

    Parameters:
        number: int

    Returns:
        True,
        False.
    """
    for divider in range(2, number // 2 + 1):
        if number % divider == 0:
            return False


def correct_answer():
    """
    Generate question number and return correct answer.

    Returns:
            cor_answer,
            question_string.
    """
    bound = (0, 3571)
    num = randint(bound[0], bound[1])
    cor_answer = 'yes' if check_prime(num) else 'no'
    return cor_answer, num
