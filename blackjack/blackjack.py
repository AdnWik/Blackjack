from exceptions import Win, Defeat
from deck import Deck
from human import Human
from croupier import Croupier


class Game:
    """Game abstract"""
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
