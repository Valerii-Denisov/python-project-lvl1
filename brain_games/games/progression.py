"""The module contains the rules of the game and its functions."""
from random import choice, randint

RULES = 'What number is missing in the progression?'
DIFFERENCE_BORDER = (0, 100)
PROGRESSION_LENGTH_BORDER = (5, 10)
INITIAL_TERM_BORDER = (0, 1000)


def get_progression(initial_term, difference, max_array_length):
    """
    Generate progression.

    Parameters:
        difference: tuple
        initial_term: tuple
        max_array_length: tuple

    Returns:
            progression.
    """
    progression_length = 0
    progression = []
    while progression_length < max_array_length:
        progression.append(str(initial_term))
        initial_term += difference
        progression_length += 1
    return progression


def stringify_progression(progression):
    """
    Turn a question progression into a string.

    Parameters:
        progression: list

    Returns:
            string.
    """
    return ' '.join(progression)


def get_game_data():
    """
    Generate question number and return correct answer.

    Returns:
            cor_answer,
            question_string.
    """
    progression_parameters = (
        randint(*INITIAL_TERM_BORDER),
        randint(*DIFFERENCE_BORDER),
        randint(*PROGRESSION_LENGTH_BORDER),
    )
    progression = get_progression(*progression_parameters)
    cor_answer_index = choice(range(progression_parameters[2]))
    question_progression = progression[:]
    question_progression[cor_answer_index] = '..'
    return (
        progression[cor_answer_index],
        stringify_progression(question_progression),
    )
