from brain_games import engine
from brain_games.games import get_question_and_right_answer


def main():
    engine.run_game(get_question_and_right_answer)


if __name__ == "__main__":
    main()