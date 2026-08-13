import secrets

DESCRIPTION = "Find the greatest common divisor of given numbers."


def find_gcd(first_number, second_number):
    while second_number != 0:
        first_number, second_number = (
            second_number,
            first_number % second_number,
        )

    return first_number


def generate_round():
    first_number = secrets.randbelow(100) + 1
    second_number = secrets.randbelow(100) + 1

    question = f"{first_number} {second_number}"
    correct_answer = find_gcd(first_number, second_number)

    return question, str(correct_answer)

