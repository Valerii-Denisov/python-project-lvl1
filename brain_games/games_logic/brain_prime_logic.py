"""The module contains the rules of the game and its functions."""
from random import randint


def printing_rule():
    """Print game rules."""
    print("Answer 'yes' if the number is prime, otherwise answer 'no'.")


def correct_answer():
    """
    Generate question number and return correct answer.

    Returns:
            cor_answer.
    """
    bound = (0, 3571)
    num = randint(bound[0], bound[1])  # noqa: S311
    step_counter = 0
    for divider in range(2, num // 2 + 1):
        if num % divider == 0:
            step_counter += 1
    print('Question: {0}'.format(num))
    cor_answer = 'yes' if step_counter <= 0 else 'no'
    return cor_answer  # noqa: WPS331


def user_answer():
    """
    Asks the user for his answer and return his.

    Returns:
            u_answer.
    """
    u_answer = input('Your answer: ')
    return u_answer  # noqa: WPS331
