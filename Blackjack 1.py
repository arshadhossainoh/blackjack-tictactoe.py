logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random
import os

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    # take a list of cards and return the score calculated from the card
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score, dealer_score):
   
    if player_score == dealer_score:
        return "Draw 🙃"
    elif dealer_score == 0:
        return "Player Lose, dealer has Blackjack 😱"
    elif player_score == 0:
        return "Player has a Blackjack 😎"
    elif player_score > 21:
        return "You went over. Player lose 😭"
    elif dealer_score > 21:
        return "You went over. dealer lose 😁"
    elif player_score > dealer_score:
        return "Player win 😃"
    else:
        return "Player lose 😤"


def play_game():
    print(logo)
    player_cards = []
    dealer_cards = []
    is_game_over = False

    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"player cards: {player_cards}, current score: {player_score}")
        print(f"dealer's first card: {dealer_cards[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            player_should_deal = input("type 'y' for another card, type 'n' to pass: ")
            if player_should_deal == "y":
                player_cards.append(deal_card())
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"    your final hand: {player_cards}, final score: {player_score}")
    print(f"    dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))

while input("do you wanna play blackjack? 'y' or 'n': ") == "y":
    os.system("cls")
    play_game()