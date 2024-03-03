import random

def computer_guess_number():
    number_to_guess = random.randint(0, 100)
    guesses = 0

    print("Welcome to the Number Guessing Game!!!!!!!!")
    print("Please think of a number between 0 and 100, and I'll try to guess it.")

    while True:
        guess = random.randint(0, 100)
        print(f"My guess is: {guess}")
        guesses += 1

        feedback = input("Is it correct, too low, or too high? ").lower()

        if feedback == "correct":
            print(f"I got it! Your number is {number_to_guess}. It took me {guesses} guesses!")
            break
        elif feedback == "too low":
            print("Okay, I'll guess higher.")
        elif feedback == "too high":
            print("Okay, I'll guess lower.")
        else:
            print("Invalid input. Please enter correct, too low, or too high.")

def main():
    computer_guess_number()

