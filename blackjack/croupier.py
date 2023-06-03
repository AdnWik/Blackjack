from player import Player


class Croupier(Player):
    """Croupier abstract"""
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Croupier'

    def __str__(self) -> str:
        return f'{self.name} | Hand power: {self.hand_power} | Hand: {self.hand}'

    def show_name(self) -> str:
        """Show name Croupier"""
        return f'{self.name}'
