import random
import os
import hangManArt
import hangManlogo
import hangManWords

print("Welcome to the Game")
print(hangManlogo.logo)

word_chosen = hangManWords.word_list[(random.randint(0, len(hangManWords.word_list) - 1))]
# word_chosen = "camel"
print(word_chosen)

blank_list = []
word_length = len(word_chosen)
print(f"word_length: {word_length}")
for i in range(0, word_length):
    blank_list.append('_')

for i in range(0, len(blank_list)):
    print(blank_list[i], end=' ')

number_of_lives = len(hangManArt.stages)
print(f"\nnumber of lives remaining: {number_of_lives}")

while number_of_lives > 0:
    position = 0
    guess = (input("\nGuess a letter: ")).lower()
    # guess.lower()
    os.system('cls')                ######## Only for windows system
    # os.system('clear')            ######## Only for Linux and Mac Os system
    print(guess)
    if guess in blank_list:
        print("You have already guessed the letter\n")
    for char in word_chosen:
        position += 1
        if guess == char:
            # print("\n",position)
            blank_list[position - 1] = char
            print("You have guessed a correct letter in the word")
    for i in blank_list:
        print(i, end=' ')

    if guess not in blank_list:
        number_of_lives -= 1
        print(f"\nyou have guessed {guess}, that's not in the word. you have only {number_of_lives} tries left.")
        print(hangManArt.stages[number_of_lives])
        if number_of_lives == 0:
            print("Man Hanged, you lost")
            break

    if '_' not in blank_list:
        print(f"\nYou have guessed the correct word. The word is {word_chosen}, You Won")
        number_of_lives = 0
