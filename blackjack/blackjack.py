from random import shuffle
"""_summary_
"""


class Card:
    """
    _summary_
    """
    def __init__(self, value, color) -> None:
        self.value = value
        self.color = color
        self.score = Card.set_score(self)

    def __repr__(self) -> str:
        return f'|{self.value}:{self.color}|'

    def __str__(self) -> str:
        return f'|{self.value:^4}:{self.color:^7}|'

    def set_score(self) -> int:
        """_summary_

        Returns:
            _type_: _description_
        """
        if isinstance(self.value, int):
            return self.value
        elif self.value != 'A':
            return 10
        else:
            return 1


class Deck:
    """_summary_
    """
    packOfCards = []

    @staticmethod
    def create_pack(number_of_packs=1):
        """
        Generate pack of cards
        """
        packs = 0
        pack_value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        pack_color = ['Karo', 'Pik', 'Trefl', 'Kier']

        while packs != number_of_packs:
            for color in pack_color:
                for value in pack_value:
                    Deck.packOfCards.append(Card(value, color))
            packs += 1

    @staticmethod
    def shuffle_cards() -> None:
        """_summary_
        """
        shuffle(Deck.packOfCards)


class Player:
    """_summary_
    """
    def __init__(self) -> None:
        self.score = 0
        self.hand_power = 0
        self.hand = []

    def calculate_hand_power(self) -> None:
        self.hand_power = sum([card.score for card in self.hand])

    def take_cards(self, number_of_cards=1) -> None:
        took_cards = 0
        while took_cards != number_of_cards:
            if len(Deck.packOfCards) > 0:
                self.hand.append(Deck.packOfCards.pop(0))
            Player.calculate_hand_power(self)
            took_cards += 1


class Human(Player):
    """_summary_

    Args:
        Player (_type_): _description_
    """
    def __init__(self, first_name, last_name, score=0) -> None:
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return (f'{self.first_name} {self.last_name} '
                f'| Hand power: {self.hand_power} | Hand: {self.hand}')


class Croupier(Player):
    """_summary_

    Args:
        Player (_type_): _description_
    """

    def __str__(self) -> str:
        return f'Croupier | Hand power: {self.hand_power} | Hand: {self.hand}'


class Game:
    """_summary_
    """
    pass


if __name__ == '__main__':
    Deck.create_pack()
    Deck.shuffle_cards()

    croupier = Croupier()
    human1 = Human('Adrian', 'W-ik')

    human1.take_cards(2)
    croupier.take_cards(2)
    
    print(croupier)
    print(human1)

    # Dobierasz czy pasujesz?
    # Koniec gdy gracz pasuje lub suma jego kart > 21
    # Krupier wygrywa gdy gracz spasuje a gracz ma mniej punktów niż 21 a on ma więcej od gracza
    # jeśli masz tylko 2 asy twoje punkty to 21
    # Jeśli as i figura twoje punkty to 21
    # jesli masz 3 karty i jedna z nich to as to as ma wartośc 1
    # jeden as to 11
