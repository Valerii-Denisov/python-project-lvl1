"""Function of greeting."""
import prompt


def welcome_user():
    """Asking name of user.Return greeting of user."""
    name = prompt.string('May I have your name? ')
    if name:
        print('Hello, {0}!'.format(name))
