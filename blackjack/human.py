from player import Player


class Human(Player):
    """ Human abstract"""
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
