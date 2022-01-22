"""The module contains the rules of the game and its functions."""
from random import choice, randint

RULE = 'What is the result of the expression?'


def correct_answer():
    """
    Generate question number and return correct answer.

    Returns:
            cor_answer,
            question_string.
    """
    bound = (0, 100)
    num1 = randint(bound[0], bound[1])
    num2 = randint(bound[0], bound[1])
    math_operator = choice(['+', '-', '*'])
    if math_operator == '+':
        cor_answer = num1 + num2
    elif math_operator == '-':
        cor_answer = num1 - num2
    else:
        cor_answer = num1 * num2
    return str(cor_answer),'{0} {2} {1}'.format(num1, num2, math_operator)
