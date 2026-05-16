# Number Guessing Game 🎯

A command-line number guessing game built with Python. Try to guess the secret number in as few attempts as possible — and beat the high score!

## How to Play

1. The computer picks a random number between **1 and 100**
2. You have **7 attempts** to guess it
3. After each guess you'll get a hint: **Too low** or **Too high**
4. Guess it correctly to record your score — fewest attempts wins!

High scores are saved locally between sessions, so the competition carries over every time you play.

## Getting Started

### Prerequisites

- Python 3.8+

No external dependencies — uses only the Python standard library.

### Installation

```bash
git clone https://github.com/penensaez/guessing-game.git
cd guessing-game
```

### Run

```bash
python guessing_game.py
```

## Example

```
Current best: 3 attempt(s)
Attempt 1 of 7 - Guess the number between 1 and 100: 50
Too low!
Attempt 2 of 7 - Guess the number between 1 and 100: 75
Too high!
Attempt 3 of 7 - Guess the number between 1 and 100: 63
You got it! You took 3 attempt(s).
```

## Built With

- [Python](https://www.python.org/)
