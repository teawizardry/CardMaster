import numpy as np
import pandas as pd
import d20 as d20

# Enter current character information here:
level = 4
name = 'Arael Lovebite'
data = 'data.xlsx'

class CardMaster:
    def __init(self, level, name, data):
        self.level = level
        self.name = name
        self.data = data
    
    def CardCollection():
        # Display your total card collection (spells known)
        card_collection = pd.read_excel(data, sheet_name='Card Collection')
        print(card_collection)
        return

    def AddCard():
        # Add a card to your collection
        return

    def BuildDeck():
        # Prepare your 20 card deck
        return

    def DrawHand():
        # Draw five cards
        return

    def DrawCard():
        # Draw one card
        return

    def DiscardPile():
        # View discard pile
        return
    
    def DiscardCard():
        # Discard card(s) from hand
        return

    def ReshuffleCard():
        # Reshuffle one card from hand into deck
        return

    def FullHouse():
        # Return 5 cards from discard to deck
        return

