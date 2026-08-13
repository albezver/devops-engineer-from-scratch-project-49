import secrets

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False

    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def generate_round():
    number = secrets.randbelow(100) + 1

    question = str(number)

    if is_prime(number):
        correct_answer = "yes"
    else:
        correct_answer = "no"

    return question, correct_answer

