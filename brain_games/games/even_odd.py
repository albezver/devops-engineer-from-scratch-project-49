import secrets

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
    return secrets.randbelow(100) + 1


def is_even(number):
    return number % 2 == 0


def generate_round():
    number = generate_question()

    if is_even(number):
        correct_answer = "yes"
    else:
        correct_answer = "no"

    return str(number), correct_answer
