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
    rejectCards = []

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
        self.stand = False

    def calculate_hand_power(self) -> None:
        if len(self.hand) > 2:  # Jeśli więcej niż 2 karty na ręce to AS = 1
            self.hand_power = sum([card.score for card in self.hand])

        else:   # Jeśli 2 karty na ręce to AS = 11
            for card in self.hand:
                if card.value == 'A':
                    card.score = 11
            self.hand_power = sum([card.score for card in self.hand])

    def check_hand(self):
        if self.hand_power == 21:
            raise Win('BLACKJACK!')
        elif self.hand_power > 21:
            set_hand = {card.value for card in self.hand}
            if 'A' in set_hand and len(set_hand) == 1:
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


class Human(Player):
    """_summary_

    Args:
        Player (_type_): _description_
    """
    def __init__(self, first_name, last_name) -> None:
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return (f'{self.first_name} {self.last_name} '
                f'| Hand power: {self.hand_power} | Hand: {self.hand}')
    
    def __repr__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Croupier(Player):
    """_summary_

    Args:
        Player (_type_): _description_
    """
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Croupier'

    def __str__(self) -> str:
        return f'{self.name} | Hand power: {self.hand_power} | Hand: {self.hand}'


class Game:
    """_summary_
    """
    def __init__(self) -> None:
        self.croupier = Croupier()
        self.players = []

    def add_players(self) -> None:
        while True:
            print('\nEnter your first name')
            first_name = input('>>> ')

            print('Enter your last name')
            last_name = input('>>> ')
            self.players.append(Human(first_name, last_name))
            print(f'Player {self.players[-1].first_name} {self.players[-1].last_name} added')
            print('\nAdd next one? (Y/n)')
            next_one = input('>>> ')
            if next_one != 'Y':
                break

    @staticmethod
    def prepare_cards() -> None:
        Deck.create_pack(3)
        Deck.shuffle_cards()


    def give_cards(self) -> None:
        for player in self.players:
            player.take_cards(2)
        self.croupier.take_cards(2)

    def clear_hands(self) -> None:
        for player in self.players:
            player.stand = False
            player.return_cards()
        self.croupier.stand = False
        self.croupier.return_cards()

    def playing(self) -> str:
        result = None
        game = True
        while game:
            for player in self.players:
                try:
                    player.check_hand()
                except Win as win:
                    result = f'{player.first_name} {win}'
                    game = False
                    break
                except Defeat as lose:
                    result = f'{player.first_name} {lose}'
                    game = False
                    break
            
            try:
                self.croupier.check_hand()
            except Win as win:
                result = f'{self.croupier.name} {win}'
                game = False
            except Defeat as lose:
                result = f'{self.croupier.name} {lose}'
                game = False

            if game != False:
                for player in self.players:
                    if player.stand == False:
                        print('\n')
                        print(player)
                        print(f'{player.first_name} Hit or Stand?')
                        print('1 - hit\n2 - Stand')
                        player_choice = int(input('>>> '))
                        if player_choice != 1:
                            player.stand = True
                        else:
                            player.take_cards()

                print(self.croupier)
                if self.croupier.hand_power < 17:
                    self.croupier.take_cards()
                else:
                    self.croupier.stand = True

                players_stand = {player.stand for player in self.players}
                if True in players_stand and len(players_stand) == 1 and self.croupier.stand == True: # jezeli gracze i krupier spasowali
                    game = False
                    high_score_player = max(self.players, key=lambda player: player.hand_power)
                    if high_score_player.hand_power > self.croupier.hand_power:
                        result = f'{high_score_player.first_name}'
                    else:
                        result = f'{self.croupier.name}'
        #TODO: Implement result when all players and Croupier stand
        return '\n' + result

if __name__ == '__main__':
    game = Game()
    game.add_players()
    game.prepare_cards()
    
    n = 0
    while n < 10:
        game.give_cards()
        print(game.playing())
        game.clear_hands()
        n += 1


    # DONE: Dobierasz czy pasujesz?
    # TODO: Koniec gdy gracz pasuje lub suma jego kart > 21
    # TODO: Krupier wygrywa gdy gracz spasuje a gracz ma mniej punktów niż 21 a on ma więcej od gracza
    # DONE: jeśli masz tylko 2 asy twoje punkty to 21
    # DONE: Jeśli as i figura twoje punkty to 21
    # DONE: jesli masz 3 karty i jedna z nich to as to as ma wartośc 1
    # DONE: jeden as to 11
