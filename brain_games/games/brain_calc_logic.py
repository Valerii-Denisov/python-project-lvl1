"""The module contains the rules of the game and its functions."""
from random import choice, randint


def printing_rule():
    """Print game rules."""
    print('What is the result of the expression?')


def correct_answer():
    """
    Generate question number and return correct answer.

    Returns:
            cor_answer.
    """
    bound = [0, 100]
    num1 = randint(bound[0], bound[1])
    num2 = randint(bound[0], bound[1])
    math_operator = choice(['+', '-', '*'])
    print('Question: {0} {2} {1}'.format(num1, num2, math_operator))
    if math_operator == '+':
        cor_answer = num1 + num2
    elif math_operator == '-':
        cor_answer = num1 - num2
    else:
        cor_answer = num1 * num2
    return str(cor_answer)


def user_answer():
    """
    Asks the user for his answer and return his.

    Returns:
            u_answer.
    """
    u_answer = input('Your answer: ')
    return u_answer
