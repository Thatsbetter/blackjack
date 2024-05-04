from deck import Deck, Player, Card
import random


def play_blackjack():
    deck = Deck()
    player = Player()
    dealer = Player()

    # Initial two cards for player and dealer
    for _ in range(2):
        player.add_card(deck.draw_card())
        dealer.add_card(deck.draw_card())

    print("Your hand:", player.show_hand(True))
    print("Dealer's hand:", dealer.show_hand())

    # Player's turn
    while input("Do you want to hit? (y/n) ").lower() == 'y':
        player.add_card(deck.draw_card())
        print("Your hand:", player.show_hand(True))
        if player.calculate_score() > 21:
            print("Bust! Your score went over 21.")
            return

    # Dealer's turn
    while dealer.calculate_score() < 17:
        dealer.add_card(deck.draw_card())

    print("Dealer's hand:", dealer.show_hand(True))

    # Determine result
    player_score = player.calculate_score()
    dealer_score = dealer.calculate_score()
    print("Your score:", player_score)
    print("Dealer's score:", dealer_score)

    if player_score > 21:
        print("You bust!")
    elif dealer_score > 21 or player_score > dealer_score:
        print("You win!")
    elif player_score < dealer_score:
        print("Dealer wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    play_blackjack()