from exceptions import Win, Defeat
from deck import Deck


class Player:
    """_summary_
    """
    def __init__(self) -> None:
        self.score = 0
        self.hand_power = 0
        self.hand = []
        self.stand = False

    def calculate_hand_power(self) -> None:
        """
        Calculate hand power from self.hand and
        set calculate value in self.hand_power
        """
        if len(self.hand) <= 2:
            for card in self.hand:
                if card.value == 'Ace':
                    card.score = 11

        self.hand_power = sum([card.score for card in self.hand])

    def check_hand(self):
        if self.hand_power == 21:
            raise Win('BLACKJACK!')
        elif self.hand_power > 21:
            _hand = {card.value for card in self.hand}
            if 'Ace' in _hand and len(_hand) == 1:
                raise Win('BLACKJACK!')
            else:
                raise Defeat('GAME OVER')

    def take_cards(self, number_of_cards=1) -> None:
        took_cards = 0
        while took_cards != number_of_cards:
            if len(Deck.packOfCards) > 0:
                self.hand.append(Deck.packOfCards.pop(0))
            Player.calculate_hand_power(self)
            took_cards += 1

    def return_cards(self) -> None:
        Deck.rejectCards.extend(self.hand)
        self.hand.clear()