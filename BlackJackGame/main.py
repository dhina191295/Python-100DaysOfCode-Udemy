############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random
import os

play_value = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
def play_blackjack():
    os.system('clear')
    if play_value != "n":
        print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    user = []
    dealer = []
    user_score = 0
    dealer_score = 0

    invalid_hand = True


    while invalid_hand:
        user.append(random.choice(cards))
        user.append(random.choice(cards))

        dealer.append(random.choice(cards))
        dealer.append(random.choice(cards))

        for i in user:
            user_score += i

        for i in dealer:
            dealer_score += i

        if user_score > 21 or dealer_score > 21:
            invalid_hand = True
            user = []
            dealer = []
        else:
            invalid_hand = False

    game_progress = True
    result = False

    print(f"Your cards: {user}, current score: {user_score}")
    print(f"Computer's first card: {dealer[0]}")
    # print(f"Computer's first card: {dealer},current score: {dealer_score}")
    if user_score == 21:
        print("you won with Blackjack")
    elif dealer_score == 21:
        print(f"Computer's first card: {dealer},current score: {dealer_score}")
        print("Computer won with BlackJack")
    else:
        game_progress = True


    while game_progress:
        pass_value = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if pass_value == "n":
            while dealer_score < 17:
                new_card= random.choice(cards)
                if new_card == 11 and dealer_score + 11 > 21:
                    dealer.append(1)
                else:
                    dealer.append(new_card)
                # print(f"computer card: {dealer}")
                dealer_score = 0
                # print(type(dealer_score))
                for i in dealer:
                    dealer_score = dealer_score + i
                if dealer_score > 21:
                    result = True
                    print("You won")
                    break
            if dealer_score >= 17:
                game_progress = False
                print(f"Your cards: {user}, current score: {user_score}")
                print(f"Computer hand: {dealer}, Computer Score: {dealer_score}")
                if user_score == dealer_score:
                    print("DRAW")
                elif dealer_score > user_score:
                    print("You lose")
                else:
                    print("You won")

        else:
            new_card= random.choice(cards)
            if new_card == 11 and dealer_score + 11 > 21:
                user.append(1)
            else:
                user.append(new_card)
            print(f"Player cards: {user}")
            user_score = 0
            for i in user:
                user_score += i
            print(f"user score: {user_score}")
            if user_score > 21:
                result= True
                print("You lose")
                break
        if result ==  True:
            game_progress = False
    new_game = input("Please type 'y' to start a new game or type 'n' to exit: ")
    if new_game == "y":
        play_blackjack()

play_blackjack()
