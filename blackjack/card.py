class InvalidCardValue(Exception):
    """Raise when card value is invalid"""


class InvalidCardColor(Exception):
    """Raise when card color is invalid"""


class Card:
    """Card abstraction"""
    possible_colors = {
        'spades': '\u2664',
        'diamonds': '\u2662',
        'hearts': '\u2661',
        'clubs': '\u2667'
        }

    possible_values = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']

    def __init__(self, value, color) -> None:
        if value not in Card.possible_values:
            raise InvalidCardValue('Invalid card value!')
        self.value = value

        if color not in Card.possible_colors:
            raise InvalidCardColor('Invalid card color!')
        self.color = color

        self.score = Card.set_score(self)

    def __repr__(self) -> str:
        return f' {self.value}  {Card.possible_colors[self.color]} '

    def __str__(self) -> str:
        return f' {self.value}  {Card.possible_colors[self.color]} '

    def set_score(self) -> int:
        """
        Set score value for all cards:
        2-10 = value from card (2-10)
        Q,J,K = 10
        A = 1

        Returns:
            int: score of card
        """
        if self.value in range(2, 11):
            return self.value
        elif self.value != 'Ace':
            return 10
        else:
            return 1
