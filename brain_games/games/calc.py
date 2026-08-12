import random

DESCRIPTION = "What is the result of the expression?"

OPERATIONS = ("+", "-", "*")


def calculate(first_number, second_number, operation):
    match operation:
        case "+":
            return first_number + second_number
        case "-":
            return first_number - second_number
        case "*":
            return first_number * second_number


def generate_round():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    operation = random.choice(OPERATIONS)

    question = f"{first_number} {operation} {second_number}"
    correct_answer = calculate(
        first_number,
        second_number,
        operation,
    )

    return question, str(correct_answer)