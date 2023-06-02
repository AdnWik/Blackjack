from deck import Deck


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

    def show_name(self) -> str:
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
    
    def show_name(self) -> str:
        return f'{self.name}'


class Game:
    """_summary_
    """
    def __init__(self) -> None:
        self.croupier = Croupier()
        self.players = []
        self.participants = []

    def add_players(self) -> None:
        """
        Create n-players and Croupier,
        next add all of them to participants list
        """
        _player_no = 1
        while True:
            print(f'\nPlayer {_player_no}')
            print('\nEnter first name')
            first_name = input('>>> ')

            print('Enter last name')
            last_name = input('>>> ')

            self.players.append(Human(first_name, last_name))
            _player_no += 1
            print(f'Player {self.players[-1].first_name} '
                  f'{self.players[-1].last_name} added'
                  f'\n\nAdd Player {_player_no}? (Y/n)')
            
            next_player = input('>>> ')
            if next_player != 'Y':
                self.participants.extend(self.players)
                self.participants.append(self.croupier)
                break

    @staticmethod
    def prepare_cards() -> None:
        Deck.create_pack(3)
        Deck.shuffle_cards()

    def give_cards(self) -> None:
        """
        Give first two cards to all of participants
        """
        for participant in self.participants:
            participant.take_cards(2)

    def clear_hands(self) -> None:
        """
        Set stand status to False and return cards
        from hand to reject_cards list for all of participants
        """
        for participant in self.participants:
            participant.stand = False
            participant.return_cards()

    def playing(self) -> str:
        result = None
        game = True
        while game:
            for participant in self.participants:
                if game is not False:
                    try:
                        participant.check_hand()
                    except Win as win:
                        participant.score += 1
                        result = f'{participant.show_name()} {win}'
                        game = False
                        break
                    except Defeat as lose:
                        #participant.score -= 1
                        result = f'{participant.show_name()} {lose}'
                        game = False
                        break

            if game is not False:
                for participant in self.participants:
                    if participant.stand is False:
                        print('\n')
                        print(participant)
                        if participant.__class__.__name__ != 'Croupier':
                            # If not Croupier
                            print(f'{participant.first_name} Hit or Stand?')
                            print('1 - hit\n2 - Stand')
                            participant_choice = int(input('>>> '))
                            if participant_choice == 1:
                                participant.take_cards()
                            else:
                                participant.stand = True
                        else:
                            # If Croupier
                            if participant.hand_power < 17:
                                participant.take_cards()
                                print(f'{participant.show_name()} take a card')
                            else:
                                participant.stand = True
                                print(f'{participant.show_name()} stand')

                participants_stand = {participant.stand
                                      for participant
                                      in self.participants}
                if True in participants_stand and len(participants_stand) == 1:
                    game = False
                    max_hand_power_participant = max(self.participants,
                                         key=lambda participant:
                                         participant.hand_power)
                    max_hand_power_participant.score += 1
                    result = f'{max_hand_power_participant.show_name()} WIN!'

        return f'\n>>>>> {result} <<<<<\n'

    def show_results(self) -> str:
        participants_sorted = sorted(self.participants,
                                     key=lambda participant:
                                     participant.score, reverse=True)
        for participant in participants_sorted:
            print(f'{participant.show_name()} SCORE:{participant.score}')

if __name__ == '__main__':
    game = Game()
    print('='*100)
    print('Welcome in BLACKJACK game!')
    print('='*100)
    game.add_players()
    game.prepare_cards()

    n = 1
    while n <= 10:
        print('='*100)
        print(f'n:{n}')
        game.give_cards()
        print(game.playing())
        game.clear_hands()
        n += 1
    game.show_results()
