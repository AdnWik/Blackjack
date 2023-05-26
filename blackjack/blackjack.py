from random import shuffle
"""_summary_
"""


class Defeat(Exception):
    """_summary_

    Args:
        Exception (_type_): _description_
    """


class Win(Exception):
    """_summary_

    Args:
        Exception (_type_): _description_
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
        if len(self.hand) > 2:  # Jeśli więcej niż 2 karty na ręce to AS = 1
            self.hand_power = sum([card.score for card in self.hand])

        else:   # Jeśli 2 karty na ręce to AS = 11
            for card in self.hand:
                if card.value == 'A':
                    card.score = 11
            self.hand_power = sum([card.score for card in self.hand])

        if self.hand_power == 21:
            raise Win('WIN!')
        elif self.hand_power > 21:
            set_hand = {card.value for card in self.hand}
            if 'A' == set_hand and len(set_hand) == 1:
                raise Win('WIN!')
            else:
                raise Defeat('Too much power')

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

    try:
        human1.take_cards(2)
    except Defeat as error:
        print(error)
    except Win as error:
        print(error)

    try:
        croupier.take_cards(2)
    except Defeat as error:
        print(error)
    except Win as error:
        print(error)

    player_choice = 0
    while player_choice != 1:
        print(croupier)
        print(human1)
        player_choice = int(input('0 - Dobierasz czy 1 - pasujesz?'))
        if player_choice != 1:
            try:
                human1.take_cards()
            except Defeat as error:
                print(error)
                player_choice = 1
            except Win as error:
                print(error)
                player_choice = 1
                

    if croupier.hand_power > human1.hand_power:
        print(f'Croupier win! C:{croupier.hand_power} -> P:{human1.hand_power}')
    else:
        print(f'Player win! P:{human1.hand_power} -> C:{croupier.hand_power}')
    # Dobierasz czy pasujesz?
    # Koniec gdy gracz pasuje lub suma jego kart > 21
    # Krupier wygrywa gdy gracz spasuje a gracz ma mniej punktów niż 21 a on ma więcej od gracza
    # jeśli masz tylko 2 asy twoje punkty to 21
    # Jeśli as i figura twoje punkty to 21
    # jesli masz 3 karty i jedna z nich to as to as ma wartośc 1
    # jeden as to 11
