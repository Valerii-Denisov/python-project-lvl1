"""The module contains the rules of the game and its functions."""
from random import randint

RULE = "Answer 'yes' if the number is prime, otherwise answer 'no'."


def correct_answer():
    """
    Generate question number and return correct answer.

    Returns:
            cor_answer,
            question_string.
    """
    bound = (0, 3571)
    num = randint(bound[0], bound[1])
    step_counter = 0
    for divider in range(2, num // 2 + 1):
        if num % divider == 0:
            step_counter += 1
    cor_answer = 'yes' if step_counter <= 0 else 'no'
    return cor_answer, num
