#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import art
print(art.logo)

# GUESS_NUMBER = random.randint(1,101)

NUMBER = random.randint(2,100)
# print(NUMBER)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")



def level_selection():
    level = ""
    while level == "":
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

        if level == "easy":
            return 10
        elif level == "hard":
            return 5
        else:
            level = ""
            print("Please choose appropriate difficulty(easy or hard).")

def game_play(attempts_available):
    while attempts_available > 0:
        print(f"You have {attempts_available} attempts remaining to guess the number.")
        guess_number = int(input("Make a guess: "))

        if guess_number > NUMBER:
            print("Too high.")
        elif guess_number < NUMBER:
            print("Too low.")
        else:
            print(f"You got it! The answer was {NUMBER}")
            break

        attempts_available -= 1
        if (attempts_available <= 0):
            print(f"The number to be guessed was {NUMBER}")
            print("You have run out of guesses, you lose")
            break
        print("Guess again")

attempts_provided = level_selection()
game_play(attempts_provided)
