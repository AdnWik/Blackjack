from random import shuffle
from card import Card


class Deck:
    """
    Deck abstract
    """
    packOfCards = []
    rejectCards = []

    @staticmethod
    def create_pack(number_of_packs=1):
        """
        Create pack of cards
        """
        packs = 0
        pack_value = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
        pack_color = ['spades', 'diamonds', 'hearts', 'clubs']

        while packs != number_of_packs:
            for color in pack_color:
                for value in pack_value:
                    Deck.packOfCards.append(Card(value, color))
            packs += 1

    @staticmethod
    def shuffle_cards() -> None:
        """
        Shuffle cards from list Deck.packOfCards
        (shuffle method from random)
        """
        shuffle(Deck.packOfCards)
