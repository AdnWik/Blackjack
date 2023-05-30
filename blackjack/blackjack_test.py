from blackjack import Deck, Card, Player


# def test_test():
    #given

    #when

    #then

def test_card_amount():
    """
    Check generated 52 unique cards in 3 packs
    """
    number_of_packs = 3
    Deck.create_pack(number_of_packs)
    score = len({(card.value, card.color) for card in Deck.packOfCards})
    assert score == 52


def test_set_score_5():
    """
    Check value for Card(5, Karo)
    """
    card_5 = Card(5, 'Karo')
    score = card_5.set_score()
    assert score == 5


def test_set_score_j():
    """
    Check value for Card(J, Pik)
    """
    card_J = Card('J', 'Pik')
    score = card_J.set_score()
    assert score == 10


def test_set_score_q():
    """
    Check value for Card(Q, Trefl)
    """
    card_Q = Card('Q', 'Trefl')
    score = card_Q.set_score()
    assert score == 10


def test_set_score_k():
    """
    Check value for Card(K, Kier)
    """
    card_K = Card('K', 'Kier')
    score = card_K.set_score()
    assert score == 10


def test_set_score_a():
    """
    Check value for Card(A, Karo)
    """
    card_A = Card('A', 'Karo')
    score = card_A.set_score()
    assert score == 1


def test_change_score_for_a_two_cards():
    """
    Check hand power for hand with two cards (one 'A' included)
    """
    player1 = Player()
    player1.hand = [Card('A', 'Kier'), Card(1, 'Pik')]
    player1.calculate_hand_power()
    score = player1.hand_power
    assert score == 12


def test_change_score_for_two_a():
    """
    Check hand power for hand with two 'A'.
    """
    player1 = Player()
    player1.hand = [Card('A', 'Kier'), Card('A', 'Pik')]
    player1.calculate_hand_power()
    score = player1.hand_power
    assert score == 22


def test_change_score_for_a_three_cards():
    """
    Check hand power for hand with three cards (one 'A' included)
    """
    player1 = Player()
    player1.hand = [Card('A', 'Kier'), Card(1, 'Pik'), Card(1, 'Karo')]
    player1.calculate_hand_power()
    score = player1.hand_power
    assert score == 3
