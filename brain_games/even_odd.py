import random


def is_even(number):
    return number % 2 == 0


def generate_question():
    return random.randint(0, 100)