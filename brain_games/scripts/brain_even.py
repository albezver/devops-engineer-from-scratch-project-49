import prompt

from brain_games.cli import welcome_user
from brain_games.even_odd import generate_question, is_even


def generate_questions(name):
    question_counter = 0

    while question_counter < 3:
        question_number = generate_question()
        print(f"Question: {question_number}")

        user_answer = prompt.string("Your answer: ") or ""

        if is_even(question_number) and user_answer.lower() == "yes":
            print("Correct!")
            question_counter += 1
        elif not is_even(question_number) and user_answer.lower() == "no":
            print("Correct!")
            question_counter += 1
        else:
            break

    if question_counter == 3:
        print(f"Congratulations, {name}!")


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    generate_questions(name)


if __name__ == "__main__":
    main()