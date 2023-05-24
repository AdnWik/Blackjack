"""_summary_
"""


class Card:
    """
    _summary_
    """

    packOfCards = []

    def __init__(self, value, color) -> None:
        self.value = value
        self.color = color
        Card.packOfCards.append(self)

    def __repr__(self) -> str:
        return f'Card|{self.value}:{self.color}'

    def __str__(self) -> str:
        return f'{self.value}:{self.color}'

    @staticmethod
    def create_pack():
        """
        Generate pack of cards
        """
        pack_value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        pack_color = ['Karo', 'Pik', 'Trefl', 'Kier']

        for color in pack_color:
            for value in pack_value:
                Card(value, color)


if __name__ == '__main__':
    Card.create_pack()

    for card in Card.packOfCards:
        print(card)
