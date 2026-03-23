
"""
Project 04 - Guess the Number Game

Description:
    Create a simple console game where the computer selects
    a random number and the player has to guess it.

Requirements:
    - The program should:
        - Choose a random number within a range (for example, 1 to 100).
        - Ask the player to guess the number.
        - After each guess, tell the player if the guess is:
            - too low
            - too high
            - correct
        - Count how many attempts the player needed.
        - End the game when the player guesses correctly and
          display the number of attempts.

Notes:
    - Use the random module to generate the secret number.
    - Input should be read from the console.
    - Handle non-numeric input gracefully (optional).

Example (expected behavior):
    I'm thinking of a number between 1 and 100.
    Take a guess: 50
    Too high!
    Take a guess: 25
    Too low!
    Take a guess: 37
    Correct! You needed 3 attempts.
"""

# TODO:
# 1. Generate a random secret number.
# 2. Ask the player to guess in a loop.
# 3. After each guess, indicate if it is too low, too high, or correct.
# 4. Count the number of attempts.
# 5. End the game when the guess is correct and show the attempt count.

import random

print("I'm thinking of a number between 1 and 100.")

# Número secreto
secret_number = random.randint(1, 100)

# Contador de intentos
attempts = 0

while True:
    guess = input("Take a guess: ")

    # Manejo de errores
    try:
        guess = int(guess)
    except:
        print("Please enter a valid number.")
        continue

    # Sumar intento
    attempts += 1

    # Lógica del juego
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Correct! You needed {attempts} attempts.")
        break