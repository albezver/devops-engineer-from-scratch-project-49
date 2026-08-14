### Hexlet tests and linter status:
[![Actions Status](https://github.com/albezver/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/albezver/devops-engineer-from-scratch-project-49/actions)
[![Quality gate status](https://sonarcloud.io/api/project_badges/measure?project=albezver_devops-engineer-from-scratch-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=albezver_devops-engineer-from-scratch-project-49)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=albezver_devops-engineer-from-scratch-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=albezver_devops-engineer-from-scratch-project-49)


## Description

Brain Games is a set of five command-line games designed to train basic math and logic skills.

Each game asks the player a series of questions. To win, the player needs to give three correct answers in a row. If the player gives a wrong answer, the game ends.

The project includes the following games:

- **Even** — determine whether a number is even.
- **Calculator** — calculate the result of an arithmetic expression.
- **GCD** — find the greatest common divisor of two numbers.
- **Progression** — find the missing number in an arithmetic progression.
- **Prime** — determine whether a number is prime.

## Installation

Make sure you have Python, [uv](https://docs.astral.sh/uv/), and Git installed.

Clone the repository:

```bash
git clone <repository-url>
```

Go to the project directory:

```bash
cd <repository-name>
```

Install the project dependencies:

```bash
make install
```

## Running the games

Run a game using `uv run`.

For example:

```bash
uv run brain-even
```

Available games:

```bash
uv run brain-even
uv run brain-calc
uv run brain-gcd
uv run brain-progression
uv run brain-prime
```

## Preview

### Brain-even Game

[![asciinema demo](https://asciinema.org/a/JOsEIcLyCvWojtgZ.svg)](https://asciinema.org/a/JOsEIcLyCvWojtgZ)

### Brain-calc Game

[![asciinema demo](https://asciinema.org/a/CK9BVDbhAUWt9WEF.svg)](https://asciinema.org/a/CK9BVDbhAUWt9WEF)

### Brain-gcd Game

[![asciinema demo](https://asciinema.org/a/l2CXVgCB0A0mshUA.svg)](https://asciinema.org/a/l2CXVgCB0A0mshUA)

### Brain-progression Game

[![asciinema demo](https://asciinema.org/a/alESeNW7mTkdqRH4.svg)](https://asciinema.org/a/alESeNW7mTkdqRH4)

### Brain-prime Game

[![asciinema demo](https://asciinema.org/a/sOB2AsYYJlR0t7es.svg)](https://asciinema.org/a/sOB2AsYYJlR0t7es)