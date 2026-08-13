import secrets


DESCRIPTION = "What number is missing in the progression?"

PROGRESSION_LENGTH = 10
MIN_START = 1
MAX_START = 20
MIN_STEP = 1
MAX_STEP = 10


def generate_progression(start, step, length):
    progression = []

    for index in range(length):
        current_element = start + index * step
        progression.append(current_element)

    return progression


def generate_round():
    start = secrets.randbelow(MAX_START - MIN_START + 1) + MIN_START
    step = secrets.randbelow(MAX_STEP - MIN_STEP + 1) + MIN_STEP

    progression = generate_progression(
        start,
        step,
        PROGRESSION_LENGTH,
    )

    hidden_index = secrets.randbelow(PROGRESSION_LENGTH)
    correct_answer = progression[hidden_index]

    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))

    return question, str(correct_answer)
