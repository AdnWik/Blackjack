from blackjack import Deck, Card, Player, Win


def test_card_amount():
    """
    Check generated 52 unique cards in 3 packs
    """
    number_of_packs = 3
    Deck.create_pack(number_of_packs)
    score = len({(card.value, card.color) for card in Deck.packOfCards})
    assert score == 52


def test_change_score_for_a_two_cards():
    """
    Check hand power for hand with two cards (one 'Ace' included)
    """
    player1 = Player()
    player1.hand = [Card('Ace', 'diamonds'), Card(2, 'clubs')]
    player1.calculate_hand_power()
    score = player1.hand_power
    assert score == 13


def test_change_score_for_two_a():
    """
    Check hand power for hand with two 'Ace'.
    """
    player1 = Player()
    player1.hand = [Card('Ace', 'diamonds'), Card('Ace', 'clubs')]
    player1.calculate_hand_power()
    score = player1.hand_power
    assert score == 22


def test_change_score_for_a_three_cards():
    """
    Check hand power for hand with three cards (one 'Ace' included)
    """
    player1 = Player()
    player1.hand = [Card('Ace', 'diamonds'), Card(2, 'clubs'), Card(2, 'hearts')]
    player1.calculate_hand_power()
    score = player1.hand_power
    assert score == 5


def test_take_cards():
    """
    Check first took card
    """
    Deck.packOfCards = []
    Deck.rejectCards = []
    Deck.create_pack()

    player1 = Player()
    player1.take_cards()

    score = (player1.hand[0].value, player1.hand[0].color)
    assert score == (2, 'spades')


def test_return_cards():
    """
    Check first rejected card
    """
    Deck.packOfCards = []
    Deck.rejectCards = []
    Deck.create_pack()

    player1 = Player()
    player1.take_cards()
    player1.return_cards()

    score = (Deck.rejectCards[0].value, Deck.rejectCards[0].color)
    assert score == (2, 'spades')
