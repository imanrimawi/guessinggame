import random

def computer_guess_number():
    lower_bound = 0
    upper_bound = 100
    number_to_guess = random.randint(lower_bound, upper_bound)
    guesses = 0

    print("Hello!!!! Welcome to the Number Guessing Game!")
    print("Please start by thinking of a number between 0 and 100, which the computer will guess.")

    while True:
        guess = random.randint(lower_bound, upper_bound)
        print(f"Computer's guess: {guess}")
        guesses += 1

        feedback = input("Is the guess correct, too low, or too high? ").upper()

        if feedback == "correct":
            print(f"Computer guessed the number {number_to_guess} correctly in {guesses} guesses!!!!")
            break
        elif feedback == "too low":
            lower_bound = guess + 1
        elif feedback == "too high":
            upper_bound = guess - 1
        else:
            print("Invalid input. Please enter either correct, too low, or too high.")

def main():
    computer_guess_number()

if __name__ == "__main__":
    main()
