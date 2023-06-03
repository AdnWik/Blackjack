    
from game import Game


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
