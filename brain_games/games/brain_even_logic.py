"""The module contains the rules of the game and its functions."""
from random import randint

GAME_RULE = "Answer 'yes' if the number is even, otherwise answer 'no'."


def correct_answer():
    """
    Generate question number and return correct answer.

    Returns:
            cor_answer,
            question_string.
    """
    lower_bound = 0
    upper_bound = 1500
    num = randint(lower_bound, upper_bound)
    cor_answer = 'yes' if num % 2 == 0 else 'no'
    return (cor_answer, 'Question: {0}'.format(num))
