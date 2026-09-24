import random as random

def number_guesser():
    secret_number = random.randint(1, 100)
    attempts = 0
    score = 100

    print("Welcome to the Number Guesser Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                score -= attempts * 10
                print(f"Your score is: {score}")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    number_guesser()