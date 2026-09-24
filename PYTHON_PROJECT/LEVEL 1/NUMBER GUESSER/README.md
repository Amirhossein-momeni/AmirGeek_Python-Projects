# Number Guesser

A simple command-line number guessing game built with Python.

The program generates a random number between 1 and 100. The user repeatedly enters guesses and receives feedback until the correct number is found.

## Features

* Generates a random number between 1 and 100
* Accepts user input from the command line
* Provides feedback for incorrect guesses
* Tracks the number of attempts
* Handles invalid input using exception handling

## Concepts Practiced

This project focuses on fundamental Python concepts:

* Functions
* Variables
* `random` module
* `while` loops
* Conditional statements
* User input with `input()`
* Type conversion with `int()`
* Exception handling with `try/except`
* `ValueError`
* f-strings
* `if __name__ == "__main__"`

## Project Structure

```text
number-guesser/
│
├── main.py
└── README.md
```

## How to Run

Make sure Python is installed on your system.

Clone the repository:

```bash
git clone <repository-url>
cd number-guesser
```

Run the application:

```bash
python main.py
```

## Example

```text
Welcome to the Number Guesser Game!
I'm thinking of a number between 1 and 100.

Enter your guess: 50
Too high! Try again.

Enter your guess: 25
Too low! Try again.

Enter your guess: 37
Congratulations! You guessed the number in 3 attempts.
```

## Learning Objective

The purpose of this project is to practice core Python programming concepts by building a small interactive command-line application.

## Future Improvements

Potential improvements include:

* Add difficulty levels
* Limit the number of attempts
* Allow multiple rounds
* Add a scoring system
* Allow the user to define the number range
* Add a replay option

## License

This project is intended for educational and practice purposes.