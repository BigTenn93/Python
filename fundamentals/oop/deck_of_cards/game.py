"""
WAR game rules
Real player vs PC
Split the deck in two
Each player places a card from the top of the deck
Highest card aces high wins the "battle"
Winner takes both cards for the round/battle, place on discard stack
Discard stack is re-shuffled when one player is out of cards
Keep playing rounds until one player has all 52 cards
"""

"""
Randomize cards into two separate dictionaries(player dict, PC dict)
Player uses a keyboard input to place a card in the "playfield"
PC places a card after player
Compare the cards, winner adds both cards to their own discard stack
Check each player to see if there or no cards left in their hand, if no cards in hand, shuffle your discard stack, this is your new hand
Repeat play until one player' discard stack is empty
"""




from classes.deck import Deck
import random

bicycle = Deck()

bicycle.shuffle_cards()
# bicycle.show_cards()

bicycle.player_hand()
bicycle.computer_hand()

# print("******")
# print("Player")
# print("******")
# bicycle.show_player_hand()
# print("******")
# print("Computer")
# print("******")
# bicycle.show_computer_hand()

# player1 = input("Please, pick your card.")
# print(f"You chose: {cards[0]}")
bicycle.player_hand()[0].card_info()
bicycle.computer_hand()[0].card_info()

player_discard_stack = bicycle.discard_stack()

player_discard_stack.discards.append(bicycle.player_hand()[0])

# player_discard_stack = []
# computer_discard_stack = []


if bicycle.player_hand()[0].point_val > bicycle.computer_hand()[0].point_val:
    player_discard_stack.append(bicycle.player_hand()[0])
elif bicycle.computer_hand()[0].point_val > bicycle.player_hand()[0].point_val:
    computer_discard_stack.append(bicycle.computer_hand()[0])


print(computer_discard_stack)
print(player_discard_stack)


# player_hand.card_info()

# player_hand = bicycle.cards[0:25]
# print(player_hand)

# computer_hand = bicycle.cards.slice(27, 52)


